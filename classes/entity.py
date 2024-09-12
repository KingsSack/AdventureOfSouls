import pygame

from classes.collider import Collider
from handlers.animations import Animations


class Entity(pygame.sprite.Sprite):
    def __init__(self, screen, width, height, hitbox_x_offset, hitbox_y_offset, hitbox_width, hitbox_height, idle_animation, walk_animation):
        super().__init__()
        self.screen = screen
        
        self.moving = False
        self.flip = False
        
        self.x, self.y = 0, 0
        self.width, self.height = width, height
        
        self.collider = Collider(self, hitbox_x_offset, hitbox_y_offset, hitbox_width, hitbox_height)
        
        self.idle_animation = idle_animation
        self.walk_animation = walk_animation
        
        self.animation_handler = Animations(self.idle_animation)
        self.sprite = self.animation_handler.get_frame()
        
        self.rect = self.sprite.get_rect()

    def draw(self):
        if self.moving == True and self.animation_handler.current_animation != self.walk_animation:
            self.animation_handler.load_animation(self.walk_animation)
        elif self.moving == False and self.animation_handler.current_animation == self.walk_animation:
            self.animation_handler.load_animation(self.idle_animation)
        
        self.screen.blit(self.sprite, self.rect)
    
    def update(self):
        self.rect.x, self.rect.y = self.x, self.y
        self.sprite = pygame.transform.flip(pygame.transform.scale(self.animation_handler.get_frame(), (self.width, self.height)), self.flip, False)
