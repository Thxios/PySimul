
import numpy as np
from typing import List, Tuple

from general.vector import *

from .config import ElectricConfig
from .charge import Charge


def coord2scr(x, y):
    # return (round(ElectricConfig.ORIGIN_X + x * ElectricConfig.SCALE),
    #         round(ElectricConfig.ORIGIN_Y + y * ElectricConfig.SCALE))
    return x, y

def scr2coord(x, y):
    # return ((x - ElectricConfig.ORIGIN_X) / ElectricConfig.SCALE,
    #         (y - ElectricConfig.ORIGIN_Y) / ElectricConfig.SCALE)
    return x, y

def electric_force(p1: Vec, q1: float, p2: Vec, q2: float) -> Tuple[Vec, Vec]:
    rel_pos = p1 - p2
    rel_unit = unit(rel_pos)
    dist_sq = np.dot(rel_pos, rel_pos)

    f = ElectricConfig.K * q1 * q2 / dist_sq
    f_ab = f * rel_unit
    f_ba = -f * rel_unit

    return f_ab.view(Vec), f_ba.view(Vec)

def check_if_collide(a: Charge, b: Charge, dt: float):
    pa_ = a.p + dt*a.v
    pb_ = b.p + dt*b.v

    if distance(a.p, b.p) <= a.r + b.r:
        return True
    if distance(pa_, pb_) <= a.r + b.r:
        return True
    return False

def apply_collision(a: Charge, b: Charge):
    rel_vec = b.p - a.p
    proj, proj_inv = proj_matrix(rel_vec)

    rel_v_a = np.dot(proj, a.v).view(Vec)
    rel_v_b = np.dot(proj, b.v).view(Vec)

    # rel_dv_a_x = 2 * b.m * (rel_v_b.x - rel_v_a.x) / (a.m + b.m)
    # rel_dv_b_x = 2 * a.m * (rel_v_a.x - rel_v_b.x) / (a.m + b.m)

    # rel_v_a.x += rel_dv_a_x
    # rel_v_b.x += rel_dv_b_x
    rel_v_a.x = -1
    rel_v_b.x = 1

    a.v = np.dot(proj_inv, rel_v_a).view(Vec)
    b.v = np.dot(proj_inv, rel_v_b).view(Vec)

def apply_electric_force(a: Charge, b: Charge, dt: float):
    f_a, f_b = electric_force(a.p, a.q, b.p, b.q)
    a.apply_force(f_a, dt)
    b.apply_force(f_b, dt)


class ForceField:
    def __init__(self, n: int = None):
        self.n_row = ElectricConfig.HEIGHT // ElectricConfig.DOTS_PIXEL_DIST + 1
        self.n_col = ElectricConfig.WIDTH // ElectricConfig.DOTS_PIXEL_DIST + 1

        # self.dot_pos: List[List[Vec]] \
        #     = [[vector(0, 0) for _ in range(self.n_col)] for _ in range(self.n_row)]
        self.dot_pos = np.zeros((self.n_row, self.n_col, 2))

        offset_y = (ElectricConfig.HEIGHT % ElectricConfig.DOTS_PIXEL_DIST) // 2
        offset_x = (ElectricConfig.WIDTH % ElectricConfig.DOTS_PIXEL_DIST) // 2

        for r in range(self.n_row):
            for c in range(self.n_col):
                scr_x = offset_x + c * ElectricConfig.DOTS_PIXEL_DIST
                scr_y = offset_y + r * ElectricConfig.DOTS_PIXEL_DIST
                self.dot_pos[r][c][0] = scr_x
                self.dot_pos[r][c][1] = scr_y

        self.pos_repeat = None
        self.n = n
        if self.n is not None:
            self.pos_repeat = np.repeat(np.expand_dims(self.dot_pos, 2), self.n, axis=2)

        self.vectors = np.zeros((self.n_row, self.n_col, 2))

    def apply_force(self, charges: List[Charge]):
        n = len(charges)

        q_arr = np.zeros((n,))
        p_arr = np.zeros((n, 2))
        for i in range(n):
            q_arr[i] = charges[i].q
            p_arr[i] = charges[i].p
        q_arr *= -ElectricConfig.K

        if self.n is not None:
            assert self.n == n, "Num objs Changed"
        else:
            self.pos_repeat = np.repeat(np.expand_dims(self.dot_pos, 2), n, axis=2)

        rel_pos = self.pos_repeat - p_arr
        dist_arr = np.power(np.einsum('rcnp,rcnp->rcn', rel_pos, rel_pos), (3/2))
        dist_arr += 1e-4
        self.vectors = np.sum(np.expand_dims(q_arr / dist_arr, 3) * rel_pos, axis=2)

    def zero_vectors(self):
        self.vectors *= 0


class ForceManager:
    def __init__(
            self,
            objects: List[Charge],
            vector_field: ForceField = None,
    ):
        self.objs = objects
        self.field = vector_field

        self.update(0)

    def update(self, dt: float):
        for i in range(len(self.objs)):
            for j in range(i+1, len(self.objs)):
                charge_a, charge_b = self.objs[i], self.objs[j]
                apply_electric_force(charge_a, charge_b, dt)

        for i in range(len(self.objs)):
            for j in range(i+1, len(self.objs)):
                charge_a, charge_b = self.objs[i], self.objs[j]
                if check_if_collide(charge_a, charge_b, dt):
                    apply_collision(charge_a, charge_b)

        drag_ratio = np.exp(np.log(ElectricConfig.DRAG_PER_SEC) * dt)
        for obj in self.objs:
            obj.apply_drag(drag_ratio)
            obj.apply_step(dt)

        if self.field:
            self.field.apply_force(self.objs)


