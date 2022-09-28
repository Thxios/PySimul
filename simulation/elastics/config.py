
from general.config import Config
from general.colors import Color
from general.vector import vector
from .collision import RigidCircle

class ElasticsConfig(Config):
    TITLE = 'Elastic Collision'
    UPDATE_PER_FRAME = 3

    FIELD_OFFSET = 50
    FIELD_WIDTH = Config.WIDTH - 2*FIELD_OFFSET
    FIELD_HEIGHT = Config.HEIGHT - 2*FIELD_OFFSET

    # objects
    OBJECTS = [
        RigidCircle(20, vector(100, 200), vector(200, -50)),
        RigidCircle(30, vector(600, 400), vector(-10, -250)),
        RigidCircle(15, vector(120, 450), vector(210, -200)),
        RigidCircle(20, vector(40, 100), vector(300, 300)),
        RigidCircle(50, vector(400, 400), vector(-500, 750)),
        RigidCircle(90, vector(600, 200), vector(-200, 300)),
    ]

    # draw configs
    CIRCLE_COLORS = [
        Color.CYAN,
        Color.RED,
        Color.GREEN,
        Color.MAGENTA,
        Color.YELLOW,
        Color.BLUE,
        Color.WHITE,
    ]
    N_COLORS = len(CIRCLE_COLORS)



