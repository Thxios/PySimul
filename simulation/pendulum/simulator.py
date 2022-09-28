import pygame as pg
from math import sin, cos, radians
from collections import deque
from typing import Deque, Tuple

from general.simulator import Simulator
from general.colors import Color

from .config import PendulumConfig


def coord2scr(x, y):
    return (round(PendulumConfig.ORIGIN_X + x * PendulumConfig.SCALE),
            round(PendulumConfig.ORIGIN_Y + y * PendulumConfig.SCALE))


class PendulumSimulator(Simulator):
    config = PendulumConfig

    def __init__(self):
        self.G = self.config.G
        self.L1, self.L2 = self.config.L1, self.config.L2
        self.M1, self.M2 = self.config.M1, self.config.M2

        self.t1 = radians(self.config.T1_0)
        self.t2 = radians(self.config.T2_0)

        self.w1 = radians(self.config.W1_0)
        self.w2 = radians(self.config.W2_0)

        self.x1 = self.L1 * sin(self.t1)
        self.y1 = self.L1 * cos(self.t1)

        self.x2 = self.x1 + self.L2 * sin(self.t2)
        self.y2 = self.y1 + self.L2 * cos(self.t2)

        self.path_surf = pg.Surface(
            (self.config.WIDTH, self.config.HEIGHT),
            pg.SRCALPHA,
            32
        )
        self.path_queue: Deque[Tuple[int, int]] = deque()
        self.path_matrix = [
            [0 for _ in range(self.config.HEIGHT)]
            for _ in range(self.config.WIDTH)]

    def update(self, dt):
        a1_n1 = -self.G * (2 * self.M1 + self.M2) * sin(self.t1)
        a1_n2 = -self.M2 * self.G * sin(self.t1 - 2 * self.t2)
        a1_n3 = -2 * sin(self.t1 - self.t2) * self.M2
        a1_n4 = self.w2 ** 2 * self.L2 + self.w1 ** 2 * self.L1 * cos(self.t1 - self.t2)

        a2_n1 = 2 * sin(self.t1 - self.t2)
        a2_n2 = self.w1 ** 2 * self.L1 * (self.M1 + self.M2)
        a2_n3 = self.G * (self.M1 + self.M2) * cos(self.t1)
        a2_n4 = self.w2 ** 2 * self.L2 * self.M2 * cos(self.t1 - self.t2)

        d = 2 * self.M1 + self.M2 - self.M2 * cos(2 * self.t1 - 2 * self.t2)
        d1 = d * self.L1
        d2 = d * self.L2

        a1 = (a1_n1 + a1_n2 + a1_n3 * a1_n4) / d1
        a2 = a2_n1 * (a2_n2 + a2_n3 + a2_n4) / d2

        self.w1 += dt * a1
        self.w2 += dt * a2

        self.t1 += dt * self.w1
        self.t2 += dt * self.w2

        self.x1 = self.L1 * sin(self.t1)
        self.y1 = self.L1 * cos(self.t1)

        self.x2 = self.x1 + self.L2 * sin(self.t2)
        self.y2 = self.y1 + self.L2 * cos(self.t2)

    def draw(self, screen):
        screen.fill(self.config.BG_COLOR)

        scr_pos1 = coord2scr(self.x1, self.y1)
        scr_pos2 = coord2scr(self.x2, self.y2)

        if self.config.SHOW_PATH_N > 0:
            px, py = scr_pos2
            self.path_queue.append(scr_pos2)
            self.path_surf.set_at(scr_pos2, self.config.PATH_COLOR)
            self.path_matrix[px][py] += 1

            if len(self.path_queue) > self.config.SHOW_PATH_N:
                lx, ly = self.path_queue.popleft()
                self.path_matrix[lx][ly] -= 1
                if self.path_matrix[lx][ly] == 0:
                    self.path_surf.set_at((lx, ly), Color.TRANSPARENT)

            screen.blit(self.path_surf, (0, 0))

        pg.draw.aaline(screen,
                       self.config.LINE_COLOR,
                       self.config.ORIGIN,
                       scr_pos1)
        pg.draw.aaline(screen,
                       self.config.LINE_COLOR,
                       scr_pos1,
                       scr_pos2)

        pg.draw.circle(screen,
                       self.config.PENDULUM_COLOR,
                       scr_pos1,
                       self.config.R1)
        pg.draw.circle(screen,
                       self.config.PENDULUM_COLOR,
                       scr_pos2,
                       self.config.R2)
