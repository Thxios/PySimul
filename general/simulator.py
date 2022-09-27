
import pygame as pg
from typing import Type
from .config import Config

class Simulator:
    config: Type[Config] = None

    def update(self, dt: float):
        raise NotImplementedError()

    def draw(self, screen: pg.Surface):
        raise NotImplementedError()

