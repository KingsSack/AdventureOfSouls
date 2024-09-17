import pygame


class Collider:
    def __init__(self, entity, x_offset, y_offset, width, height):
        self.entity = entity
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.x = self.x_offset
        self.y = self.y_offset
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def collides(self, other: 'Collider') -> bool:
        return (self.rect.colliderect(other.rect))
    
    def update(self):
        self.x = self.entity.x + self.x_offset
        self.y = self.entity.y + self.y_offset
        self.rect.x, self.rect.y = self.x, self.y
