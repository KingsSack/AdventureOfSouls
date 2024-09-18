import pygame

from handlers.animations import Animations


class Alert(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x, self.y = x, y
        self.width, self.height = 48, 48
        self.animation_handler = Animations("alert")
        self.sprite = self.animation_handler.get_frame()
    
    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))
    
    def update(self):
        self.sprite = pygame.transform.scale(self.animation_handler.get_frame(), (self.width, self.height))
