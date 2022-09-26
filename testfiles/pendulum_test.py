import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from simulation.pendulum.simulator import PendulumSimulator
from app import Window

if __name__ == '__main__':
    simulator = PendulumSimulator()
    app = Window(simulator)

    app.run()
