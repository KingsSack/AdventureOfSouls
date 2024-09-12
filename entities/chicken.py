import pygame

from classes.entity import Entity


class Chicken(Entity):
    def __init__(self, screen, x, y):
        super().__init__(screen, 48, 48, 6, 6, 42, 42, 'chicken_idle', 'chicken_walk')
        self.x, self.y = self.rect.x, self.rect.y = x, y
