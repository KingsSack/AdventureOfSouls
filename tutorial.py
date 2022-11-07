import pygame
import game
import savedata

def new_arrow(rotation, rect_x, rect_y, type):
    arrow = game.Arrow(64, 64, rotation, type)
    arrow.rect.x = rect_x
    arrow.rect.y = rect_y
    game.tutorial_sprites_list.add(arrow)
    # if stage == 1:
    #     game.stage1_sprites_list.add(arrow)
    # if stage == 2:
    #     game.stage2_sprites_list.add(arrow)
    # if stage == 3:
    #     game.stage3_sprites_list.add(arrow)

def stage_one():
    new_arrow(90, game.width / 2 - 32, game.height - 40, 1)
    
    savedata.tutorial_level = 1
