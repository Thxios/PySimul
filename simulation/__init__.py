
from .pendulum.simulator import PendulumSimulator
from .elastics.simulator import ElasticsSimulator
from .electric.simulator import ElectricSimulator


simulations = {
    'pendulum': PendulumSimulator,
    'elastics': ElasticsSimulator,
    'electric': ElectricSimulator
}

simulation_names = list(simulations.keys())

__all__ = [
    'simulations',
    'simulation_names',
]

