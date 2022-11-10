import time
import pygame
import game
import instantiate
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
    
    # project loaded
    print(f'Project loaded in {time.time() - t}s')

    # game class
    class GameState():
        def __init__(self):
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
            
            # change current state 
            self.state = current_stage
            
            # remove old sprites
            game.map_sprites.empty()
            game.enemy_sprite_list.empty()
            game.item_sprite_list.empty()
            game.tutorial_sprites_list.empty()
            
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
            game.map_sprites.draw(screen)
            game.item_sprite_list.draw(screen)
            game.enemy_sprite_list.draw(screen)
            game.character_sprite_list.draw(screen)
            self.user_interface()
            game.tutorial_sprites_list.draw(screen)
            
            # update sprites
            game.main_character.update()
            game.map_sprites.update()
            game.enemy_sprite_list.update()
            game.tutorial_sprites_list.update()
            
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
            
            if savedata.tutorial_level == 0:
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
            health_background = pygame.image.load("menu/ui_background.png")
            health_background = pygame.transform.scale(health_background, (140, 140))
            screen.blit(health_background, (12, -32))
            
            settings_btn = pygame.image.load("menu/SquareMenu.png")
            settings_btn = pygame.transform.scale(settings_btn, (48, 48))
            screen.blit(settings_btn, (4, height - 52))
            settings_icon = pygame.image.load("menu/Settings.png")
            settings_icon = pygame.transform.scale(settings_icon, (36, 36))
            screen.blit(settings_icon, (10, height - 46))

            inventory_btn = pygame.image.load("menu/SquareMenu.png")
            inventory_btn = pygame.transform.scale(inventory_btn, (48, 48))
            screen.blit(inventory_btn, (56, height - 52))
            inventory_icon = pygame.image.load("menu/Backpack.png")
            inventory_icon = pygame.transform.scale(inventory_icon, (36, 36))
            screen.blit(inventory_icon, (61.5, height - 46))
            
            spellbook_btn = pygame.image.load("menu/SquareMenu.png")
            spellbook_btn = pygame.transform.scale(spellbook_btn, (48, 48))
            screen.blit(spellbook_btn, (108, height - 52))
            spellbook_icon = pygame.image.load("menu/Spellbook.png")
            spellbook_icon = pygame.transform.scale(spellbook_icon, (36, 36))
            screen.blit(spellbook_icon, (114, height - 46))

            spell1 = pygame.image.load("menu/SquareMenu.png")
            spell1 = pygame.transform.scale(spell1, (48, 48))
            screen.blit(spell1, (width / 2 - 76, height - 52))
            if savedata.spell_slot1 == "empty":
                lock1 = pygame.image.load("menu/Lock.png")
                lock1 = pygame.transform.scale(lock1, (36, 36))
                screen.blit(lock1, (width / 2 - 70, height - 46))
            else:
                if savedata.spell_slot1 == "fireball":
                    fireball = pygame.image.load("menu/Firebomb.png")
                    fireball = pygame.transform.scale(fireball, (36, 36))
                    screen.blit(fireball, (width / 2 - 70, height - 46))
                if savedata.spell_slot1 == "thunder":
                    thunderbomb = pygame.image.load("menu/Bolt.png")
                    thunderbomb = pygame.transform.scale(thunderbomb, (36, 36))
                    screen.blit(thunderbomb, (width / 2 - 70, height - 46))

            spell2 = pygame.image.load("menu/SquareMenu.png")
            spell2 = pygame.transform.scale(spell2, (48, 48))
            screen.blit(spell2, (width / 2 - 24, height - 52))
            if savedata.spell_slot2 == "empty":
                lock2 = pygame.image.load("menu/Lock.png")
                lock2 = pygame.transform.scale(lock2, (36, 36))
                screen.blit(lock2, (width / 2 - 18, height - 46))
            else:
                if savedata.spell_slot2 == "fireball":
                    fireball = pygame.image.load("menu/Firebomb.png")
                    fireball = pygame.transform.scale(fireball, (36, 36))
                    screen.blit(fireball, (width / 2 - 18, height - 46))
                if savedata.spell_slot2 == "thunder":
                    thunderbomb = pygame.image.load("menu/Firebomb.png")
                    thunderbomb = pygame.transform.scale(thunderbomb, (36, 36))
                    screen.blit(thunderbomb, (width / 2 - 18, height - 46))

            spell3 = pygame.image.load("menu/SquareMenu.png")
            spell3 = pygame.transform.scale(spell3, (48, 48))
            screen.blit(spell3, (width / 2 + 28, height - 52))
            if savedata.spell_slot3 == "empty":
                lock3 = pygame.image.load("menu/Lock.png")
                lock3 = pygame.transform.scale(lock3, (36, 36))
                screen.blit(lock3, (width / 2 + 34, height - 46))
            else:
                if savedata.spell_slot3 == "fireball":
                    fireball = pygame.image.load("menu/Firebomb.png")
                    fireball = pygame.transform.scale(fireball, (36, 36))
                    screen.blit(fireball, (width / 2 + 34, height - 46))
                if savedata.spell_slot3 == "thunder":
                    thunderbomb = pygame.image.load("menu/Firebomb.png")
                    thunderbomb = pygame.transform.scale(thunderbomb, (36, 36))
                    screen.blit(thunderbomb, (width / 2 + 34, height - 46))
        
        def stage_manager(self):
            # stages
            if self.state == game.stages["menu"][0]:
                self.menu()
            
            if self.state == game.stages["ardale"][0]:
                self.ardale_spawn()
            
            if self.state == game.stages["ardale"][1]:
                self.ardale_center()

            if self.state == game.stages["ardale"][2]:
                self.ardale_countryside()
            
            if self.state == game.stages["flowerfield"][0]:
                self.flowerfield_entrance()

    game_stage = GameState()

    while game_stage.running:
        # tick
        pygame.time.delay(7)
        
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
