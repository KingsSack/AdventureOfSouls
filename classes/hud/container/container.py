import pygame


class Container(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, sprite):
        super().__init__()
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.sprite = sprite
