from json import load
import time
import pygame
import game
import instantiate
import interface
import collisions
import savedata
import tutorial
import console

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

def main():
    # load
    t = time.time()
    time.sleep(.1)

    # game start
    pygame.init()

    size = width, height = 852, 480
    speed = [2, 2] 
    green = 25, 77, 0
    black = 0, 0, 0
    ground = [(153, 77, 0), (140, 255, 25), (77, 25, 0)]

    # surface
    screen = pygame.display.set_mode(size)
    
    # window settings
    pygame_icon = pygame.image.load("WizardHead.png")
    pygame.display.set_icon(pygame_icon)
    pygame.display.set_caption("Adventure of Souls")
    
    # fonts
    smallfont = pygame.font.SysFont('Corbel', 35)
    text = smallfont.render('Play' , True , green)
    
    # sprites
    drawable_sprites = [game.map_sprites, game.item_sprite_list, game.enemy_sprite_list, game.character_sprite_list]
    updatable_sprites = [game.main_character, game.map_sprites, game.enemy_sprite_list, game.tutorial_sprites_list]
    level_sprites = [game.map_sprites, game.item_sprite_list, game.enemy_sprite_list, game.tutorial_sprites_list]
    
    # project loaded
    print(f'Project loaded in {time.time() - t}s')

    # game class
    class GameState():
        def __init__(self):
            # state functions
            self.state_functions = {
                game.stages["menu"][0]: self.menu,
                game.stages["ardale"][0]: self.ardale_spawn,
                game.stages["ardale"][1]: self.ardale_center,
                game.stages["ardale"][2]: self.ardale_countryside,
                game.stages["flowerfield"][0]: self.flowerfield_entrance,
            }
            
            # menu
            self.state = game.stages["menu"][0]
            
            # music
            # self.music()
            
            # running
            self.running = True
        
        def music(self):
            # play music
            pygame.mixer.music.load("Dynamaxed ▸ Lavender Town (Red & Blue) copy.mp3")
            pygame.mixer.music.play()
        
        def change_stage(self, current_stage, old_stage):
            # change last stage
            instantiate.last_stage = old_stage
            savedata.isbackdrop = False
            
            # change current state 
            self.state = current_stage
            
            # remove old sprites
            for i in level_sprites:
                i.empty()
            
            # create new sprites
            game.current_stage = current_stage
            
            if current_stage == game.stages["ardale"][0]:
                instantiate.ardale_spawn()
            
            if current_stage == game.stages["ardale"][1]:
                instantiate.ardale_center()
            
            if current_stage == game.stages["ardale"][2]:
                instantiate.ardale_countryside()
            
            if current_stage == game.stages["flowerfield"][0]:
                instantiate.flowerfield_entrance()
        
        def level(self):
            # draw sprites
            for i in drawable_sprites:
                i.draw(screen)
            
            # update sprites
            for i in updatable_sprites:
                i.update()
            
            self.user_interface()
            game.tutorial_sprites_list.draw(screen)
            
            # detect gui's
            if game.gui_open == "spellbook":
                instantiate.spellbook()
            if game.gui_open == "inventory":
                instantiate.inventory()
            if game.gui_open == "false":
                game.check_attacks()
            
            # detect collisions
            collisions.detect_collisions()
        
        def menu(self):
            # fill screen
            screen.fill(green)
            
            # head animation
            game.headrect = game.headrect.move(speed)
            if game.headrect.left < 0 or game.headrect.right > width:
                speed[0] = -speed[0]
            if game.headrect.top < 0 or game.headrect.bottom > height:
                speed[1] = -speed[1]

            screen.blit(game.head, game.headrect)
            
            # button text
            pygame.draw.rect(screen, black, [width / 2 - 50, height / 2 - 23, 100, 46], 0, 4)
            screen.blit(text, (width / 2 - 24, height / 2 - 12))
            
            # flip display
            pygame.display.flip()
        
        def ardale_spawn(self):
            # stage functions
            screen.fill(ground[0])
            game.ardale_spawn()
            self.level()
            
            if savedata.tutorial_level < 2:
                tutorial.ardale_spawn(1)

            # stage changes
            if game.main_character.rect.y < -130 and 400 >= game.main_character.rect.x >= 300:
                self.change_stage(game.stages["ardale"][1], 1)
            
            if height / 2 - 100 <= game.main_character.rect.y <= height / 2 + 100 and game.main_character.rect.x >= 750:
                self.change_stage(game.stages["ardale"][2], 1)
            
            # flip display
            pygame.display.flip()
        
        def ardale_center(self):
            # stage functions
            screen.fill(ground[0])
            game.ardale_center()
            self.level()
            
            if savedata.tutorial_level < 3:
                tutorial.ardale_center(1)
            
            # stage changes
            if game.main_character.rect.y > 400 and 400 >= game.main_character.rect.x >= 300:
                self.change_stage(game.stages["ardale"][0], 2)
            
            if height / 2 - 100 <= game.main_character.rect.y <= height / 2 + 100 and game.main_character.rect.x <= -2:
                self.change_stage(game.stages["flowerfield"][0], 2)
                
            # flip display
            pygame.display.flip()
        
        def ardale_countryside(self):
            # stage functions
            screen.fill(ground[0])
            game.ardale_countryside()
            self.level()
            
            # stage changes
            if height / 2 - 100 <= game.main_character.rect.y <= height / 2 + 100 and game.main_character.rect.x <= -2:
                self.change_stage(game.stages["ardale"][0], 3)
            
            # flip display
            pygame.display.flip()

        def flowerfield_entrance(self):
            # stage functions
            screen.fill(ground[1])
            game.flowerfield_entrance()
            
            self.level()
            
            # stage changes
            if height / 2 - 100 <= game.main_character.rect.y <= height / 2 + 100 and game.main_character.rect.x >= width - 100:
                self.change_stage(game.stages["ardale"][1], 4)
            
            # flip display
            pygame.display.flip()
        
        def user_interface(self):
            # health background
            interface.load_and_blit_image(screen, "menu/ui_background.png", (140, 140), (12, -32))
            
            # settings
            interface.load_and_blit_image(screen, "menu/SquareMenu.png", interface.BACKGROUND_SIZE, (4, height - 52))
            interface.load_and_blit_image(screen, "menu/Settings.png", interface.ICON_SIZE, (10, height - 46))
            
            # backpack
            interface.load_and_blit_image(screen, "menu/SquareMenu.png", interface.BACKGROUND_SIZE, (56, height - 52))
            interface.load_and_blit_image(screen, "menu/Backpack.png", interface.ICON_SIZE, (61.5, height - 46))
            
            # spellbook
            interface.load_and_blit_image(screen, "menu/SquareMenu.png", interface.BACKGROUND_SIZE, (108, height - 52))
            interface.load_and_blit_image(screen, "menu/Spellbook.png", interface.ICON_SIZE, (114, height - 46))
            
            # spell slots
            for i, spell in enumerate([savedata.spell_slot1, savedata.spell_slot2, savedata.spell_slot3]):
                spell_image_path = interface.SPELL_IMAGES[spell]
                interface.load_and_blit_image(screen, "menu/SquareMenu.png", interface.BACKGROUND_SIZE, (width / 2 - 76 + i * 52, height - 52))
                interface.load_and_blit_image(screen, spell_image_path, interface.ICON_SIZE, (width / 2 - 70 + i * 52, height - 46))
        
        def stage_manager(self):
            # stages
            if self.state in self.state_functions:
                self.state_functions[self.state]()

    game_stage = GameState()

    while game_stage.running:
        # tick
        pygame.time.delay(int(1000 / 60))
        
        # detect window closing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_stage.running = False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game_stage.running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_stage.state == game.stages["menu"][0]:
                    if width / 2 - 50 <= mouse[0] <= width / 2 + 50 and height / 2 - 23 <= mouse[1] <= height / 2 + 23:
                        game_stage.change_stage(game.stages["ardale"][0], game.stages["menu"][0])
                else:
                    game.ui_buttons()
        
        # main
        game_stage.stage_manager()
        
        mouse = pygame.mouse.get_pos()
    
    # quit game
    pygame.quit()

if __name__ == "__main__":
    main()
