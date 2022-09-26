
import pygame as pg

from general.simulator import Simulator
from general.colors import Color

from .config import ElasticsConfig
from .collision import RigidCircle, CollisionManager


class ElasticsSimulator(Simulator):
    config = ElasticsConfig

    def __init__(self):
        self.manager = CollisionManager(
            (ElasticsConfig.FIELD_WIDTH, ElasticsConfig.FIELD_HEIGHT),
            ElasticsConfig.OBJECTS
        )
        self.field_surface = pg.Surface(
            (ElasticsConfig.FIELD_WIDTH, ElasticsConfig.FIELD_HEIGHT),
            pg.SRCALPHA,
            32
        )
        self.field_surface.fill(Color.TRANSPARENT)

    def update(self, dt: float):
        for _ in range(ElasticsConfig.N_STEP):
            self.manager.update(dt / ElasticsConfig.N_STEP)

    def draw(self, screen: pg.Surface):
        screen.fill(ElasticsConfig.BG_COLOR)
        self.field_surface.fill(Color.TRANSPARENT)

        for i in range(len(self.manager.objs)):
            color = ElasticsConfig.CIRCLE_COLORS[i % ElasticsConfig.N_COLORS]
            circle = self.manager.objs[i]
            pg.draw.circle(self.field_surface, color, circle.p, circle.r)

        screen.blit(self.field_surface, (ElasticsConfig.FIELD_OFFSET, ElasticsConfig.FIELD_OFFSET))
        pg.draw.rect(screen, Color.WHITE,
                     (ElasticsConfig.FIELD_OFFSET, ElasticsConfig.FIELD_OFFSET,
                      ElasticsConfig.FIELD_WIDTH, ElasticsConfig.FIELD_HEIGHT), 1)
