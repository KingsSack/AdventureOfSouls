import pygame
import game
import instantiate

direction = "up"


class Hitbox(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
  
        self.rect = self.image.get_rect()
    
    def update(self, pos_x, pos_y):
        self.rect.x, self.rect.y = pos_x, pos_y

hitbox = Hitbox(43, 96.75)


def stage_one():
    if pygame.sprite.spritecollideany(hitbox, game.stage1_sprites_list):
        if direction == "left":
            game.main_character.rect.x += 3
        if direction == "right":
            game.main_character.rect.x -= 3
        if direction == "down":
            game.main_character.rect.y += 3
        if direction == "up":
            game.main_character.rect.y -= 3

def stage_two():
    if pygame.sprite.spritecollideany(hitbox, game.stage2_sprites_list):
        if direction == "left":
            game.main_character.rect.x += 3
        if direction == "right":
            game.main_character.rect.x -= 3
        if direction == "down":
            game.main_character.rect.y += 3
        if direction == "up":
            game.main_character.rect.y -= 3

def stage_three():
    if pygame.sprite.spritecollideany(hitbox, game.stage3_sprites_list):
        if direction == "left":
            game.main_character.rect.x += 3
        if direction == "right":
            game.main_character.rect.x -= 3
        if direction == "down":
            game.main_character.rect.y += 3
        if direction == "up":
            game.main_character.rect.y -= 3
