import pygame
import game
import savedata

size = width, height = 852, 480
screen = pygame.display.set_mode(size)

def new_arrow(rotation, rect_x, rect_y, type):
    arrow = game.Arrow(64, 64, rotation, type)
    arrow.rect.x = rect_x
    arrow.rect.y = rect_y
    game.tutorial_sprites_list.add(arrow)

def new_text(text, character):
    if not savedata.isbackdrop:
        backdrop = game.TutorialBackdrop()
        backdrop.rect.x = width / 2 - 230
        backdrop.rect.y = height / 2 + 20
        game.tutorial_sprites_list.add(backdrop)
        
        savedata.isbackdrop = True
    
    
    if character == "narrator":
        """ coming soon """
    
    font = pygame.font.Font("fonts/PixelFont.ttf", 30)
    
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = screen.get_size()
    pos = width / 2 - 218, height / 2 + 55
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, (240, 240, 255))
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            screen.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
    

def ardale_spawn(type):
    if type == 0:
        new_arrow(90, game.width / 2 - 32, game.height - 40, 1)
    else:
        new_text(f'Welcome to Ardale! Ardale\nis a town full of creative\npeople with many different\nprofessions. You are our\nnew adventurer!', "narrator")
    
    # savedata.tutorial_level = 1
