
from typing import Union, Tuple
from general.vector import *

class RigidCircle:
    def __init__(
            self,
            radius: float,
            pos: Union[Vec, Tuple[float, float]],
            mass: float = None,
            velocity: Union[Vec, Tuple[float, float]] = None,
    ):
        self.r = radius

        self.m = mass
        if self.m is None:
            self.m = self.r

        self.p = pos
        if not isinstance(self.p, Vec):
            self.p = vector(*self.p)

        self.v = velocity
        if self.v is None:
            self.v = vector(0, 0)
        if not isinstance(self.v, Vec):
            self.v = vector(*self.v)

class Manager:
    def __init__(self):
        pass


