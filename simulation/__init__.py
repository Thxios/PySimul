
from .pendulum.simulator import PendulumSimulator
from .elastics.simulator import ElasticsSimulator


simulations = {
    'pendulum': PendulumSimulator,
    'elastics': ElasticsSimulator,
}

simulation_names = list(simulations.keys())

__all__ = [
    'simulations',
    'simulation_names',
]

