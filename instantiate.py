from cmath import rect
import pygame
import time
import game
import main
import savedata

size = width, height = 852, 480
direction = "right"
last_stage = 1

def new_house(rotation, rect_x, rect_y, stage):
    current_house = game.House(506, 320, rotation)
    current_house.rect.x = rect_x
    current_house.rect.y = rect_y
    if stage == 1:
        game.stage1_sprites_list.add(current_house)
    if stage == 2:
        game.stage2_sprites_list.add(current_house)

def new_tree(tree_type, width, height, rotation, rect_x, rect_y, stage):
    current_tree = game.Tree(tree_type, width, height, rotation)
    current_tree.rect.x = rect_x
    current_tree.rect.y = rect_y
    if stage == 1:
        game.stage1_sprites_list.add(current_tree)
    if stage == 2:
        game.stage2_sprites_list.add(current_tree)

def new_slime(rect_x, rect_y, stage):
    current_slime = game.Slime(stage)
    current_slime.rect.x = rect_x
    current_slime.rect.y = rect_y
    if stage == 1:
        game.stage1_sprites_list.add(current_slime)
    if stage == 2:
        game.stage2_sprites_list.add(current_slime)
    if stage == 3:
        game.stage3_sprites_list.add(current_slime)

def stage_one():
    new_house(0, width / 2 - 380, height / 2 - 345, 1)
    new_house(0, width / 2 - 112, height / 2 - 345, 1)
    
    new_tree(1, 103, 129, 0, width / 2 + 225, height / 2 - 240, 1)
    new_tree(1, 103, 129, 0, width / 2 + 275, height / 2 - 166, 1)
    new_tree(1, 108, 134, 0, width / 2 + 333, height / 2 - 220, 1)
    new_tree(2, 168, 187, 0, width / 2 - 400, height / 2 - 240, 1)

    if last_stage == 2:
        game.main_character.rect.x = width / 2 - 86
        game.main_character.rect.y = height / 2 - 300
    else:
        game.main_character.rect.x = width / 2 - 86
        game.main_character.rect.y = height / 2 - 86
    game.character_sprite_list.add(game.main_character)

def stage_two():
    game.spell_object1.rect.x = width / 2 - 32
    game.spell_object1.rect.y = height / 2 - 32
    game.stage2_sprites_list.add(game.spell_object1)

    game.spell_glow1.rect.x = width / 2 - 32
    game.spell_glow1.rect.y = height / 2 - 42
    game.stage2_sprites_list.add(game.spell_glow1)

    if last_stage == 1:
        game.main_character.rect.x = width / 2 - 86
        game.main_character.rect.y = height / 2 + 150
    else:
        game.main_character.rect.x = width / 2 - 86
        game.main_character.rect.y = height / 2 - 86
    game.character_sprite_list.add(game.main_character)

def stage_three():
    new_slime(width / 2 - 250, height / 2 - 500, 3)

    if last_stage == 1:
        game.main_character.rect.x = width / 2 - 86
        game.main_character.rect.y = height / 2 + 150
    else:
        game.main_character.rect.x = width / 2 - 86
        game.main_character.rect.y = height / 2 - 86
    game.character_sprite_list.add(game.main_character)

pygame.init()

ui_background_color = 51, 34, 0
ui_main_color = 102, 51, 0
ui_title_color = 255, 217, 179

undertale_font = pygame.font.Font("fonts/UndertaleFont.ttf", 21)
inventory_title = undertale_font.render("Inventory", True, ui_title_color)
spellbook_title = undertale_font.render("Spellbook", True, ui_title_color)

inventory_sprites = pygame.sprite.Group()

def new_tab(type, rect_x, rect_y):
    current_tab = game.InvTab(type)
    current_tab.rect.x = rect_x
    current_tab.rect.y = rect_y
    inventory_sprites.add(current_tab)

def inventory():
    pygame.draw.rect(game.screen, ui_background_color, [width / 2 - 110, height / 2 - 190, 220, 40], 0, 6)
    pygame.draw.rect(game.screen, ui_background_color, [width / 2 - 190, height / 2 - 155, 380, 310], 0, 7)
    pygame.draw.rect(game.screen, ui_main_color, [width / 2 - 185, height / 2 - 150, 370, 300], 0, 5)
    game.screen.blit(inventory_title, (width / 2 - 104, height / 2 - 180))
    
    height_var = 105
    width_var = -3.5
    
    for i in range(35):
        inventory_slot = pygame.image.load("menu/Slot.png")
        inventory_slot = pygame.transform.scale(inventory_slot, (48, 48))
        if i == 7:
            height_var = 54
            width_var = -3.5
        if i == 14:
            height_var = 2
            width_var = -3.5
        if i == 21:
            height_var = -50
            width_var = -3.5
        if i == 28:
            height_var = -102
            width_var = -3.5
        if i == 35:
            height_var = -154
            width_var = -3.5
        width_var += 1
        game.screen.blit(inventory_slot, (width / 2 - (width_var * (48 + 3)), height / 2 - height_var))
    
    new_tab("backpack", width / 2 - 100, height / 2 - 105)
    
    close_menu = pygame.image.load("menu/CloseMenu.png")
    close_menu = pygame.transform.scale(close_menu, (48, 48))
    game.screen.blit(close_menu, (width / 2 + 132, height / 2 - 204))

def spellbook():
    pygame.draw.rect(game.screen, ui_background_color, [width / 2 - 110, height / 2 - 190, 220, 40], 0, 6)
    pygame.draw.rect(game.screen, ui_background_color, [width / 2 - 190, height / 2 - 155, 380, 310], 0, 7)
    pygame.draw.rect(game.screen, ui_main_color, [width / 2 - 185, height / 2 - 150, 370, 300], 0, 5)
    game.screen.blit(spellbook_title, (width / 2 - 98, height / 2 - 180))
    
    height_var = 135
    width_var = -2.5
    
    for i in range(20):
        spell_slot = pygame.image.load("menu/Slot.png")
        spell_slot = pygame.transform.scale(spell_slot, (64, 64))
        if i == 5:
            height_var = 66
            width_var = -2.5
        if i == 10:
            height_var = -3
            width_var = -2.5
        if i == 15:
            height_var = -72
            width_var = -2.5
        width_var += 1
        game.screen.blit(spell_slot, (width / 2 - (width_var * (64 + 8)), height / 2 - height_var))
    
    if savedata.fireball_spell == 1:
        fireball1 = pygame.image.load("menu/FirebombLevel1Icon.png")
        fireball1 = pygame.transform.scale(fireball1, (52, 52))
        game.screen.blit(fireball1, (width / 2 - 174, height / 2 - 130))
    
    close_menu = pygame.image.load("menu/CloseMenu.png")
    close_menu = pygame.transform.scale(close_menu, (48, 48))
    game.screen.blit(close_menu, (width / 2 + 132, height / 2 - 204))
