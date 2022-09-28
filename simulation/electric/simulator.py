
import pygame as pg
from colorsys import hsv_to_rgb
from typing import Tuple

from general.simulator import Simulator
from general.vector import *
from general.colors import Color

from .config import ElectricConfig
from .manager import ForceManager, ForceField


def clamp(val, minimum, maximum):
    return min(max(val, minimum), maximum)

def draw_vec(surface: pg.Surface, vec: Vec, start: Tuple[int, int]):
    f_min, f_max = ElectricConfig.FORCE_MIN, ElectricConfig.FORCE_MAX

    mag = magnitude(vec)
    mag_clamped = clamp(mag, f_min, f_max)

    hue = (2 / 3) * (f_max - mag_clamped) / (f_max - f_min)
    color_float = hsv_to_rgb(hue, 1, 1)
    color = tuple(map(lambda x: round(255 * x), color_float))

    end = vector(*start) + ElectricConfig.VECTOR_LENGTH * unit(vec)
    pg.draw.aaline(surface, color, start, end)


class ElectricSimulator(Simulator):
    config = ElectricConfig

    def __init__(self):
        initial_objs = ElectricConfig.OBJECTS
        self.field = ForceField(len(initial_objs)) if ElectricConfig.DRAW_FORCE_FIELD else None
        self.manager = ForceManager(
            initial_objs,
            self.field,
        )

    def update(self, dt: float):
        self.manager.update(dt)

    def draw(self, screen: pg.Surface):
        screen.fill(ElectricConfig.BG_COLOR)

        if self.field:
            for r in range(self.field.n_row):
                for c in range(self.field.n_col):
                    draw_vec(screen,
                             self.field.vectors[r][c],
                             self.field.dot_pos[r][c])

        for obj in self.manager.objs:
            color = Color.RED if obj.q > 0 else Color.CYAN
            pg.draw.circle(screen, color, obj.p, obj.r)


