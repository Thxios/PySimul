
from typing import Union, Tuple, List

from general.vector import *


class Charge:
    def __init__(
            self,
            charge: float,
            pos: Union[Vec, Tuple[float, float]],
            velocity: Union[Vec, Tuple[float, float]] = None,
            mass: float = None,
            radius: float = None,
    ):
        self.q = charge

        self.m = mass
        if self.m is None:
            self.m = 10 * abs(self.q)

        self.r = radius
        if self.r is None:
            self.r = abs(self.m)

        self.p = pos
        if not isinstance(self.p, Vec):
            self.p = vector(*self.p)

        self.v = velocity
        if self.v is None:
            self.v = vector(0, 0)
        if not isinstance(self.v, Vec):
            self.v = vector(*self.v)

    def apply_force(self, force: Vec, dt: float):
        self.v += dt * force / self.m

    def apply_drag(self, drag_ratio: float):
        self.v *= drag_ratio

    def apply_step(self, dt):
        self.p += dt * self.v

