
import numpy as np
from typing import Union, Tuple, List
from general.vector import *

class RigidCircle:
    def __init__(
            self,
            radius: float,
            pos: Union[Vec, Tuple[float, float]],
            velocity: Union[Vec, Tuple[float, float]] = None,
            mass: float = None,
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

    def apply_step(self, dt):
        self.p += dt * self.v


def check_if_collide(a: RigidCircle, b: RigidCircle, dt: float):
    pa_ = a.p + dt*a.v
    pb_ = b.p + dt*b.v

    # if distance(a.p, b.p) <= a.r + b.r:
    #     return True
    if distance(pa_, pb_) <= a.r + b.r:
        return True
    return False

def apply_collision(a: RigidCircle, b: RigidCircle):
    rel_vec = b.p - a.p
    proj, proj_inv = proj_matrix(rel_vec)

    rel_v_a = np.dot(proj, a.v).view(Vec)
    rel_v_b = np.dot(proj, b.v).view(Vec)

    rel_dv_a_x = 2 * b.m * (rel_v_b.x - rel_v_a.x) / (a.m + b.m)
    rel_dv_b_x = 2 * a.m * (rel_v_a.x - rel_v_b.x) / (a.m + b.m)

    rel_v_a.x += rel_dv_a_x
    rel_v_b.x += rel_dv_b_x

    a.v = np.dot(proj_inv, rel_v_a).view(Vec)
    b.v = np.dot(proj_inv, rel_v_b).view(Vec)


class CollisionManager:
    def __init__(
            self,
            size: Tuple[int, int],
            objects: List[RigidCircle],
    ):
        self.width, self.height = size
        self.objs = objects

    def collide_border(self, obj: RigidCircle, dt: float):
        new_pos = obj.p + dt * obj.v
        if new_pos.x - obj.r <= 0 or new_pos.x + obj.r >= self.width:
            obj.v.x = -obj.v.x
        if new_pos.y - obj.r <= 0 or new_pos.y + obj.r >= self.height:
            obj.v.y = -obj.v.y

    def update(self, dt: float):
        for i in range(len(self.objs)):
            for j in range(i+1, len(self.objs)):
                circle_a, circle_b = self.objs[i], self.objs[j]
                if check_if_collide(circle_a, circle_b, dt):
                    apply_collision(circle_a, circle_b)

        for obj in self.objs:
            self.collide_border(obj, dt)
            obj.apply_step(dt)


