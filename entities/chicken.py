import pygame

from classes.entity import Entity


class Chicken(Entity):
    def __init__(self, screen, x, y):
        super().__init__(screen, 'chicken_idle', 'chicken_walk')
        self.rect.x, self.rect.y = x, y
        
    def update(self):
        self.sprite = pygame.transform.flip(pygame.transform.scale(self.animation_handler.get_frame(), (48, 48)), self.flip, False)
