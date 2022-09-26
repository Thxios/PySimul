from simulation.elastics.simulator import ElasticsSimulator
from app import Window

if __name__ == '__main__':
    simulator = ElasticsSimulator()
    app = Window(simulator)

    app.run()

