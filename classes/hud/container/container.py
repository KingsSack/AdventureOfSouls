import pygame


class Container(pygame.sprite.Sprite):
    def __init__(self, screen, width, height, sprite, num_slots: tuple, contents=[]):
        super().__init__()
        self.screen = screen
        
        self.width, self.height = width, height
        
        self.x = (self.screen.get_width() / 2) - (self.width / 2)
        self.y = (self.screen.get_height() / 2) - (self.height / 2)
        
        self.sprite = sprite
        
        self.num_rows, self.num_cols = num_slots
        self.contents = contents
