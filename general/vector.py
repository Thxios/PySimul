
import numpy as np
from typing import Tuple


class Vec(np.ndarray):
    @property
    def x(self):
        return self[0]
    @property
    def y(self):
        return self[1]
    @x.setter
    def x(self, value):
        self[0] = value
    @y.setter
    def y(self, value):
        self[1] = value


def arr(x, y) -> np.ndarray:
    return np.array([x, y], dtype=float)

def vector(x, y) -> Vec:
    return np.array([x, y], dtype=float).view(Vec)

def magnitude(v: Vec):
    return np.sqrt(np.dot(v, v))

def unit(v: Vec) -> Vec:
    mag = magnitude(v)
    if mag == 0:
        return v
    return v / mag

def distance(a: Vec, b: Vec) -> float:
    return magnitude(a - b)

def proj_matrix(vec: Vec) -> Tuple[np.ndarray, np.ndarray]:
    u = unit(vec)
    _mat = np.array([
        [u.x, u.y],
        [-u.y, u.x]
    ])
    _inv = np.array([
        [u.x, -u.y],
        [u.y, u.x]
    ])
    return _mat, _inv

