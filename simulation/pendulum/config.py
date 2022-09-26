
from general.config import Config
from general.colors import Color


class PendulumConfig(Config):
    TITLE = 'Double Pendulum'

    # constants
    G = 9.81

    L1 = 1
    L2 = 0.95

    M1 = 10
    M2 = 10

    # initial states (in degrees)
    T1_0 = -90
    T2_0 = -120

    W1_0 = -90
    W2_0 = -90

    # draw configs
    LINE_COLOR = Color.WHITE
    PENDULUM_COLOR = Color.GRAY75

    SCALE = 150
    R1 = M1
    R2 = M2

    ORIGIN_X = Config.WIDTH // 2
    ORIGIN_Y = Config.HEIGHT - 100 - int(SCALE * (L1 + L2))
    ORIGIN = (ORIGIN_X, ORIGIN_Y)


