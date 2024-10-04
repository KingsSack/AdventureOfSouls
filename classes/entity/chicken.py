from classes.collider import Collider
from classes.entity.entity import Entity


class Chicken(Entity):
    def __init__(self, screen, x, y):
        super().__init__(
            screen,
            x=x,
            y=y,
            width=48,
            height=48,
            hitbox=Collider(self, 6, 6, 42, 42),
            idle_animation='chicken_idle',
            walk_animation='chicken_walk'
        )
