import pygame

from handlers.animations import Animations


class Entity(pygame.sprite.Sprite):
    def __init__(self, screen, idle_animation, walk_animation):
        super().__init__()
        self.screen = screen
        
        self.image = None
        self.moving = False
        self.flip = False
        
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
