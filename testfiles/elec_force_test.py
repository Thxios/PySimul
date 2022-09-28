from colorsys import hsv_to_rgb

from general.vector import *
from simulation.electric.charge import electric_force
from simulation.electric.simulator import draw_vec
# from simulation.electric.config import ElectricConfig

def clamp(val, minimum, maximum):
    return min(max(val, minimum), maximum)

if __name__ == '__main__':
    p1 = vector(0, 0)
    q1 = 1

    p2 = vector(2, 2)
    q2 = -2

    f1, f2 = electric_force(p1, q1, p2, q2)
    print(f'f1 {f1}')
    print(f'f2 {f2}')

    mag = 5
    fmin, fmax = 0, 5
    mag_clamped = clamp(mag, fmin, fmax)
    print(f'mag_clamp {mag_clamped}')
    hue = (2/3) * (fmax-mag_clamped)/(fmax - fmin)
    print(f'hue {hue}')
    color_float = hsv_to_rgb(hue, 1, 1)
    print(color_float)
    color = tuple(map(lambda x: round(255 * x), color_float))
    print(hue, color)

