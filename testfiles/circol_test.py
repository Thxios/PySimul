
import numpy as np
from simulation.elastics.collision import *

if __name__ == '__main__':
    np.set_printoptions(precision=3)

    a = RigidCircle(
        1,
        vector(0, 0),
        velocity=vector(20, 0),
    )
    b = RigidCircle(
        10,
        vector(10, 10),
    )

    print('before col')
    print(f'v_a {a.v}')
    print(f'v_b {b.v}')
    CollisionManager.apply_collision(a, b)
    print('after col')
    print(f'v_a {a.v}')
    print(f'v_b {b.v}')


