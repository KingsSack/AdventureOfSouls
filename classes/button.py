import re
import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, screen, font, text, color, background_color, x, y, width, height):
        super().__init__()
        self.screen = screen
        self.font = font
        self.color = color
        self.background_color = background_color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.text = font.render(text, True, color)
        self.x_offset = (width - self.text.get_width()) / 2
        self.y_offset = (height - self.text.get_height()) / 2
    
    def resize(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.x_offset = (width - self.text.get_width()) / 2
        self.y_offset = (height - self.text.get_height()) / 2
    
    def draw(self):
        pygame.draw.rect(self.screen, self.background_color, [self.x, self.y, self.width, self.height], 0, 4)
        self.screen.blit(self.text, (self.x + self.x_offset, self.y + self.y_offset))
    
    def update(self, mouse, events):
        mouse_x, mouse_y = mouse
        if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    return True
        return False
