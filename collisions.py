import pygame
import game
import savedata

# irection = "up"


class Hitbox(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        # self.image.fill((0, 0, 0))
        
        # pygame.draw.rect(self.image, (0, 0, 0), pygame.Rect(0, 0, width, height))
  
        self.rect = self.image.get_rect()
    
    def update(self, pos_x, pos_y):
        self.rect.x, self.rect.y = pos_x, pos_y

hitbox = Hitbox(43, 94)


def detect_collisions():
    if pygame.sprite.spritecollideany(hitbox, game.map_sprites):
        sprite = pygame.sprite.spritecollideany(hitbox, game.map_sprites)
        
        if hitbox.rect.x > sprite.rect.x + sprite.width - 4:
            game.main_character.rect.x += 3
        if hitbox.rect.x < sprite.rect.x:
            game.main_character.rect.x -= 3
        if hitbox.rect.y > sprite.rect.y + sprite.height - 4:
            game.main_character.rect.y += 3
        if hitbox.rect.y < sprite.rect.y:
            game.main_character.rect.y -= 3
