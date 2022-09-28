
from general.config import Config
from general.vector import *

from .charge import Charge

class ElectricConfig(Config):
    TITLE = 'Electric Field'

    # constants
    K = 1000000
    DRAG_PER_SEC = 0.9

    # initial state
    OBJECTS = [
        Charge(1, vector(100, 200)),
        Charge(-2, vector(300, 150)),
        Charge(1, vector(320, 20)),
        Charge(-1.5, vector(150, 400)),
        Charge(1, vector(600, 300)),
        Charge(1, vector(800, 600)),
        Charge(-1, vector(750, 350)),
        Charge(-1.5, vector(650, 350)),
    ]

    # vector field
    DRAW_FORCE_FIELD = True
    FORCE_MIN = 0
    FORCE_MAX = 100
    DOTS_PIXEL_DIST = 50
    VECTOR_LENGTH = 30

    # draw configs
    SCALE = 150

    ORIGIN_X = Config.WIDTH // 2
    ORIGIN_Y = Config.HEIGHT // 2
    ORIGIN = (ORIGIN_X, ORIGIN_Y)
