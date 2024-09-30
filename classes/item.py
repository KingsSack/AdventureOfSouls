import pygame

from classes.rarity import Rarity


class Item(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, icon, rarity: Rarity):
        super().__init__()
        self.screen = screen

        self.x, self.y = x, y

        self.icon = icon
        self.icon_rect = self.icon.get_rect()
        
        self.rarity = rarity
