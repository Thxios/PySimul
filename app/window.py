
import pygame as pg
import time
from typing import Type, Union

from general.config import Config
from general.simulator import Simulator

config: Type[Config] = Config

class Window:
    def __init__(self, simulator: Simulator = None):
        pg.init()

        # noinspection PyTypeChecker
        self.screen: pg.Surface = None

        if simulator and simulator.config:
            global config
            config = simulator.config

        self.running = False
        self.playing = False
        self.simulator: Simulator = simulator

    def run(self):
        prev_time = time.time()
        sum_ftime = 0
        dt = 1 / config.FPS
        clock = pg.time.Clock()
        cnt = 0

        self.screen = pg.display.set_mode((config.WIDTH, config.HEIGHT), pg.SRCALPHA, 32)
        pg.display.set_caption(config.TITLE)
        self.draw()

        self.running = True

        while self.running:
            cnt += 1
            start_time = time.time()

            self.mainloop(dt)

            end_time = time.time()
            sum_ftime += end_time - start_time

            if cnt % config.FPS == 0:
                mean_ftime = sum_ftime / config.FPS
                if sum_ftime == 0:
                    fps = 100000
                else:
                    fps = 1 / mean_ftime
                pg.display.set_caption(
                    f'{config.TITLE} - fps: {fps:.0f} ftime: {1000*mean_ftime:.3f}ms')
                sum_ftime = 0

            clock.tick(config.FPS)
            dt = end_time - prev_time
            prev_time = end_time


    def mainloop(self, dt):
        self.handle_event()

        if self.playing:
            self.update(dt)
            self.draw()

    def handle_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.playing = not self.playing

            elif event.type == pg.KEYUP:
                pass

            elif event.type == pg.MOUSEBUTTONDOWN:
                pass

            elif event.type == pg.MOUSEBUTTONUP:
                pass

    def update(self, dt):
        if self.simulator:
            self.simulator.update(dt)

    def draw(self):
        # self.screen.fill(config.BG_COLOR)
        if self.simulator:
            self.simulator.draw(self.screen)

        pg.display.flip()
