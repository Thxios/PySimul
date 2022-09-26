
import pygame as pg


class Simulator:
    config = None

    def update(self, dt: float):
        raise NotImplementedError()

    def draw(self, screen: pg.Surface):
        raise NotImplementedError()

