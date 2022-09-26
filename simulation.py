import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import argparse
from simulation import simulation_names, simulations
from app import Window



parser = argparse.ArgumentParser(
    description='Simulations using Pygame',
)
parser.add_argument(
    'SimulationType',
    type=str,
    choices=simulation_names,
    help='simulation type to visualize',
)


if __name__ == '__main__':
    args = parser.parse_args()

    simulator = simulations[args.SimulationType]
    Window(simulator()).run()

