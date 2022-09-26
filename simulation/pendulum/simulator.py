
import pygame as pg
from math import sin, cos, radians

from general.simulator import Simulator

from .config import PendulumConfig


class PendulumSimulator(Simulator):
    def __init__(self):
        self.G = PendulumConfig.G
        self.L1, self.L2 = PendulumConfig.L1, PendulumConfig.L2
        self.M1, self.M2 = PendulumConfig.M1, PendulumConfig.M2

        self.t1 = radians(PendulumConfig.T1_0)
        self.t2 = radians(PendulumConfig.T2_0)

        self.w1 = radians(PendulumConfig.W1_0)
        self.w2 = radians(PendulumConfig.W2_0)

        self.x1 = self.L1 * sin(self.t1)
        self.y1 = self.L1 * cos(self.t1)

        self.x2 = self.x1 + self.L2 * sin(self.t2)
        self.y2 = self.y1 + self.L2 * cos(self.t2)

    def update(self, dt):
        a1_n1 = -self.G*(2 * self.M1 + self.M2)*sin(self.t1)
        a1_n2 = -self.M2*self.G*sin(self.t1 - 2*self.t2)
        a1_n3 = -2*sin(self.t1 - self.t2)*self.M2
        a1_n4 = self.w2**2*self.L2 + self.w1**2*self.L1*cos(self.t1 - self.t2)
    
        a2_n1 = 2*sin(self.t1-self.t2)
        a2_n2 = self.w1**2*self.L1*(self.M1 + self.M2)
        a2_n3 = self.G*(self.M1 + self.M2)*cos(self.t1)
        a2_n4 = self.w2**2*self.L2*self.M2*cos(self.t1-self.t2)
    
        d = 2*self.M1 + self.M2 - self.M2*cos(2*self.t1 - 2*self.t2)
        d1 = d * self.L1
        d2 = d * self.L2
    
        a1 = (a1_n1 + a1_n2 + a1_n3*a1_n4)/d1
        a2 = a2_n1*(a2_n2 + a2_n3 + a2_n4)/d2
    
        self.w1 += dt*a1
        self.w2 += dt*a2
    
        self.t1 += dt*self.w1
        self.t2 += dt*self.w2
    
        self.x1 = self.L1 * sin(self.t1)
        self.y1 = self.L1 * cos(self.t1)
    
        self.x2 = self.x1 + self.L2 * sin(self.t2)
        self.y2 = self.y1 + self.L2 * cos(self.t2)

    def draw(self, screen):
        scr_pos1 = self.coord2scr(self.x1, self.y1)
        scr_pos2 = self.coord2scr(self.x2, self.y2)

        pg.draw.aaline(screen,
                       PendulumConfig.LINE_COLOR,
                       PendulumConfig.ORIGIN,
                       scr_pos1)
        pg.draw.aaline(screen,
                       PendulumConfig.LINE_COLOR,
                       scr_pos1,
                       scr_pos2)

        pg.draw.circle(screen,
                       PendulumConfig.PENDULUM_COLOR,
                       scr_pos1,
                       PendulumConfig.R1)
        pg.draw.circle(screen,
                       PendulumConfig.PENDULUM_COLOR,
                       scr_pos2,
                       PendulumConfig.R2)

    @staticmethod
    def coord2scr(x, y):
        return (round(PendulumConfig.ORIGIN_X + x * PendulumConfig.SCALE),
                round(PendulumConfig.ORIGIN_Y + y * PendulumConfig.SCALE))

