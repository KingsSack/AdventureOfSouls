from cmath import rect
from socket import AI_NUMERICHOST
import pygame
import game
import instantiate

direction = "up"

# def collided(sprite, other):
#     """Check if the hitboxes of the two sprites collide."""
#     return sprite.hitbox.colliderect(other.rect)

def stage_one():
    # print(game.main_character.rect.x)
    # print(game.main_character.rect.y)
    
    def collide_rect(rect1, rect2, rect3, rect4):
        if rect3 < game.main_character.rect.y < rect4 and rect1 < game.main_character.rect.x < (rect1 + 4):
            game.main_character.rect.x += 3
        if rect3 < game.main_character.rect.y < rect4 and (rect2 + 4) < game.main_character.rect.x < rect2:
            game.main_character.rect.x -= 3
        if rect3 < game.main_character.rect.y < (rect3 + 4) and rect1 > game.main_character.rect.x > rect2:
            game.main_character.rect.y += 3
        if (rect4 + 4) < game.main_character.rect.y < rect4 and rect1 > game.main_character.rect.x > rect2:
            game.main_character.rect.y -= 3
    
    # print(game.stage1_sprites_list.sprites())
    # print(pygame.sprite.spritecollideany(game.main_character, game.stage1_sprites_list))
    
    if pygame.sprite.spritecollideany(game.main_character, game.stage1_sprites_list):
    # if pygame.sprite.spritecollide(game.main_character, game.stage1_sprites_list, False, collided):
        if direction == "left":
            game.main_character.rect.x += 3
        if direction == "right":
            game.main_character.rect.x -= 3
        if direction == "down":
            game.main_character.rect.y += 3
        if direction == "up":
            game.main_character.rect.y -= 3
        
    
    # if -125 < game.main_character.rect.y < 70 and 290 > game.main_character.rect.x > 270:
    #     game.main_character.rect.x += 3
    # if -125 < game.main_character.rect.y < 70 and 120 > game.main_character.rect.x > 100:
    #     game.main_character.rect.x -= 3
    # if 65 < game.main_character.rect.y < 85 and 280 > game.main_character.rect.x > 120:
    #     game.main_character.rect.y += 3
    # if -144 < game.main_character.rect.y < -124 and 280 > game.main_character.rect.x > 120:
    #     game.main_character.rect.y -= 3
    
    # if -125 < game.main_character.rect.y < 70 and 385 > game.main_character.rect.x > 365:
    #     game.main_character.rect.x -= 3
    # if -125 < game.main_character.rect.y < 70 and 550 > game.main_character.rect.x > 530:
    #     game.main_character.rect.x += 3
    # if 65 < game.main_character.rect.y < 85 and 550 > game.main_character.rect.x > 370:
    #     game.main_character.rect.y += 3
    # if -144 < game.main_character.rect.y < -124 and 550 > game.main_character.rect.x > 370:
    #     game.main_character.rect.y -= 3
    
    # if -10 < game.main_character.rect.y < 70 and -6 > game.main_character.rect.x > -10:
    #     game.main_character.rect.x -= 3
    # if -10 < game.main_character.rect.y < 70 and 48 > game.main_character.rect.x > 44:
    #     game.main_character.rect.x += 3
    # if 70 < game.main_character.rect.y < 74 and 48 > game.main_character.rect.x > -10:
    #     game.main_character.rect.y += 3
    # if -30 < game.main_character.rect.y < -26 and 48 > game.main_character.rect.x > -10:
    #     game.main_character.rect.y -= 3
