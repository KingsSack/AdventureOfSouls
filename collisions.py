import pygame
import game

def stage_one():
    # print(game.main_character.rect.x)
    # print(game.main_character.rect.y)
    
    if -125 < game.main_character.rect.y < 70 and 290 > game.main_character.rect.x > 270:
        game.main_character.rect.x += 3
    if -125 < game.main_character.rect.y < 70 and 120 > game.main_character.rect.x > 100:
        game.main_character.rect.x -= 3
    if 65 < game.main_character.rect.y < 85 and 280 > game.main_character.rect.x > 120:
        game.main_character.rect.y += 3
    if -144 < game.main_character.rect.y < -124 and 280 > game.main_character.rect.x > 120:
        game.main_character.rect.y -= 3
    
    if -125 < game.main_character.rect.y < 70 and 385 > game.main_character.rect.x > 365:
        game.main_character.rect.x -= 3
    if -125 < game.main_character.rect.y < 70 and 550 > game.main_character.rect.x > 530:
        game.main_character.rect.x += 3
    if 65 < game.main_character.rect.y < 85 and 550 > game.main_character.rect.x > 370:
        game.main_character.rect.y += 3
    if -144 < game.main_character.rect.y < -124 and 550 > game.main_character.rect.x > 370:
        game.main_character.rect.y -= 3
    
    if -10 < game.main_character.rect.y < 70 and -6 > game.main_character.rect.x > -10:
        game.main_character.rect.x -= 3
    if -10 < game.main_character.rect.y < 70 and 48 > game.main_character.rect.x > 44:
        game.main_character.rect.x += 3
    if 70 < game.main_character.rect.y < 74 and 48 > game.main_character.rect.x > -10:
        game.main_character.rect.y += 3
    if -30 < game.main_character.rect.y < -26 and 48 > game.main_character.rect.x > -10:
        game.main_character.rect.y -= 3
