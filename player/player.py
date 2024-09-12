import pygame

from classes.entity import Entity


class Player(Entity):
    def __init__(self, screen, savedata):
        super().__init__(screen, 128, 128, 32, 64, 64, 64, 'player_idle', 'player_walk')
        self.savedata = savedata
        
        self.max_health = savedata.data.get('health', 100)
        self.speed = savedata.data.get('speed', 5)
        self.power = savedata.data.get('power', 5)
        self.defense = savedata.data.get('defense', 5)
        self.inventory = savedata.data.get('inventory', [])
        self.in_combat = savedata.data.get('in_combat', False)
        
        self.rect.x, self.rect.y = self.x, self.y = (self.screen.get_width() / 2) - 64, (self.screen.get_height() / 2) - 96

    def move(self, pressed_keys):
        if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            self.moving = True
        else:
            self.moving = False
        
        if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
            self.y -= self.speed
        if pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
            self.y += self.speed
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            self.flip = True
            self.x -= self.speed
        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            self.flip = False
            self.x += self.speed

    def update(self, pressed_keys):
        super().update()
        self.move(pressed_keys)
