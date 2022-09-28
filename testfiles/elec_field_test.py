
import numpy as np

from general.vector import *
from simulation.electric.manager import ForceField
from simulation.electric.charge import Charge


if __name__ == '__main__':
    field = ForceField()
    np.set_printoptions(precision=2)

    charges = [
        Charge(1, vector(100, 200)),
        Charge(-2, vector(300, 150)),
        Charge(1, vector(320, 20)),
        Charge(-1.5, vector(150, 400)),
        Charge(1, vector(600, 300)),
        Charge(-1, vector(750, 350)),
    ]

    field.apply_force_all(charges)
    print(field.vectors[0][2])
    field.zero_vectors()
    for charge in charges:
        field.apply_force(charge)
    print(field.vectors[0][2])


