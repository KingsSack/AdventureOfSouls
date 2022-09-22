from os import kill
import time
import sys
import pygame
import game
import instantiate
import collisions
import savedata
import console
import animations

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
    print(f'project loaded in {time.time() - t}s')

    # game start
    pygame.init()

    size = width, height = 852, 480
    speed = [2, 2]
    green = 25, 255, 25
    black = 0, 0, 0
    ground = 153, 77, 0
    path = 153, 102, 0

    screen = pygame.display.set_mode(size)

    pygame_icon = pygame.image.load("WizardHead.png")
    pygame.display.set_icon(pygame_icon)
    pygame.display.set_caption("Adventure of Souls")

    smallfont = pygame.font.SysFont('Corbel',35)
    text = smallfont.render('Play' , True , green)

    class GameState():
        def __init__(self):
            self.state = game.stages[1]
        
        def change_stage(self, current_stage):
            if current_stage == game.stages[2]:
                instantiate.stage_one()
            
            if current_stage == game.stages[3]:
                instantiate.stage_two()
            
            if current_stage == game.stages[4]:
                instantiate.stage_three()
        
        def menu(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
        
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if width / 2 - 50 <= mouse[0] <= width / 2 + 50 and height / 2 - 23 <= mouse[1] <= height / 2 + 23:
                        self.state = game.stages[2]
                        game_stage.change_stage(game.stages[2])
            
            game.headrect = game.headrect.move(speed)
            if game.headrect.left < 0 or game.headrect.right > width:
                speed[0] = -speed[0]
            if game.headrect.top < 0 or game.headrect.bottom > height:
                speed[1] = -speed[1]

            screen.fill(green)
            screen.blit(game.head, game.headrect)

            pygame.draw.rect(screen, black, [width / 2 - 50, height / 2 - 23, 100, 46], 0, 4)
            screen.blit(text, (width / 2 - 24, height / 2 - 12))

            pygame.display.flip()
        
        def stage_one(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game.ui_buttons()
                    
                    print("mouse clicked")

            screen.fill(ground)
            game.stage_one()
            game.stage1_sprites_list.draw(screen)
            game.character_sprite_list.draw(screen)
            self.user_interface()
            
            game.main_character.update()

            collisions.stage_one()
            if game.gui_open == "spellbook":
                instantiate.spellbook()
            if game.gui_open == "inventory":
                instantiate.inventory()
            if game.gui_open == "false":
                game.check_attacks()

            if game.main_character.rect.y < -130 and 400 >= game.main_character.rect.x >= 300:
                instantiate.last_stage = 1
                self.state = game.stages[3]
                self.change_stage(game.stages[3])
            
            if height / 2 - 100 <= game.main_character.rect.y <= height / 2 + 100 and game.main_character.rect.x >= 750:
                instantiate.last_stage = 1
                self.state = game.stages[4]
                self.change_stage(game.stages[4])

            pygame.display.flip()
        
        def stage_two(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game.ui_buttons()

            screen.fill(ground)
            game.stage_two()
            game.stage2_sprites_list.draw(screen)
            game.character_sprite_list.draw(screen)
            self.user_interface()
            
            game.main_character.update()
            
            if game.gui_open == "spellbook":
                instantiate.spellbook()
            if game.gui_open == "inventory":
                instantiate.inventory()
                instantiate.inventory_sprites.draw()
            if game.gui_open == "false":
                game.check_attacks()
            
            if game.main_character.rect.y > 400 and 400 >= game.main_character.rect.x >= 300:
                instantiate.last_stage = 2
                self.state = game.stages[2]
                self.change_stage(game.stages[2])

            pygame.display.flip()
        
        def stage_three(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game.ui_buttons()
            
            screen.fill(ground)
            game.stage3_sprites_list.draw(screen)
            game.character_sprite_list.draw(screen)
            self.user_interface()
            
            game.main_character.update()
            
            if game.gui_open == "spellbook":
                instantiate.spellbook()
            if game.gui_open == "inventory":
                instantiate.inventory()
            if game.gui_open == "false":
                game.check_attacks()
            
            pygame.display.flip()
        
        def user_interface(self):
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
            if self.state == "menu":
                self.menu()
            
            if self.state == "stage_one":
                game.stage1_sprites_list.update()
                # console.commands.tick()
                self.stage_one()
            
            if self.state == "stage_two":
                game.stage2_sprites_list.update()
                # console.commands.tick()
                self.stage_two()

            if self.state == "stage_three":
                game.stage3_sprites_list.update()
                # console.commands.tick()
                self.stage_three()

    game_stage = GameState()

    while True:
        game_stage.stage_manager()
        mouse = pygame.mouse.get_pos()

if __name__ == "__main__":
    main()
