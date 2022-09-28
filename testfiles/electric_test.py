from simulation.electric.simulator import ElectricSimulator
from app import Window

if __name__ == '__main__':
    simulator = ElectricSimulator()
    app = Window(simulator)

    app.run()

