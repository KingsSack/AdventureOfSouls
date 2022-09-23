import pygame
import time
import main
import instantiate
import animations
import map
import savedata

stages = {1: "menu", 2: "stage_one", 3: "stage_two", 4: "stage_three"}
size = width, height = 852, 480
screen = pygame.display.set_mode(size)

green = 25, 255, 25

stage1_sprites_list = pygame.sprite.Group()
stage2_sprites_list = pygame.sprite.Group()
stage3_sprites_list = pygame.sprite.Group()
character_sprite_list = pygame.sprite.Group()
enemy_sprite_list = pygame.sprite.Group()
item_sprite_list = pygame.sprite.Group()
user_interface_sprite_list = pygame.sprite.Group()

head = pygame.image.load("WizardHead.png")
head = pygame.transform.scale(head, (100, 100))
headrect = head.get_rect()

gui_open = "false"

tab = "backpack"

class MainCharacter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # animations.idle_right_index = 0
        # animations.idle_left_index = 0
        # animations.walk_right_index = 0
        # animations.walk_left_index = 0
        if animations.attacking == "false":
            if instantiate.direction == "left":
                self.image = animations.idle_left_images[animations.idle_left_index]
                self.image = pygame.transform.scale(self.image, (172, 172))
            else:
                self.image = animations.idle_right_images[animations.idle_right_index]
                self.image = pygame.transform.scale(self.image, (172, 172))

        self.rect = self.image.get_rect()
        screen.blit(self.image, self.rect)
    
    def moveRight(self, pixels):
        self.rect.x += pixels
        instantiate.direction = "right"
        animations.walk_right_index += 1
        if animations.walk_right_index >= len(animations.walk_right_images):
            animations.walk_right_index = 0
        self.image = animations.walk_right_images[animations.walk_right_index]
        self.image = pygame.transform.scale(self.image, (172, 172))
    
    def moveLeft(self, pixels):
        self.rect.x -= pixels
        instantiate.direction = "left"
        animations.walk_left_index += 1
        if animations.walk_left_index >= len(animations.walk_left_images):
            animations.walk_left_index = 0
        self.image = animations.walk_left_images[animations.walk_left_index]
        self.image = pygame.transform.scale(self.image, (172, 172))
    
    def moveForward(self, speed):
        self.rect.y += speed * speed / 10
        if instantiate.direction == "left":
            animations.walk_left_index += 1

            if animations.walk_left_index >= len(animations.walk_left_images):
                animations.walk_left_index = 0
            
            self.image = animations.walk_left_images[animations.walk_left_index]
        else:
            animations.walk_right_index += 1

            if animations.walk_right_index >= len(animations.walk_right_images):
                animations.walk_right_index = 0
            
            self.image = animations.walk_right_images[animations.walk_right_index]
        self.image = pygame.transform.scale(self.image, (172, 172))
    
    def moveBack(self, speed):
        self.rect.y -= speed * speed / 10
        if instantiate.direction == "left":
            animations.walk_left_index += 1

            if animations.walk_left_index >= len(animations.walk_left_images):
                animations.walk_left_index = 0
            
            self.image = animations.walk_left_images[animations.walk_left_index]
        else:
            animations.walk_right_index += 1

            if animations.walk_right_index >= len(animations.walk_right_images):
                animations.walk_right_index = 0
            
            self.image = animations.walk_right_images[animations.walk_right_index]
        self.image = pygame.transform.scale(self.image, (172, 172))
    
    def idle(self):
        if instantiate.direction == "left":
            animations.idle_left_index += 1

            if animations.idle_left_index >= len(animations.idle_left_images):
                animations.idle_left_index = 0
            
            self.image = animations.idle_left_images[animations.idle_left_index]
        else:
            # print(animations.idle_right_index)
            animations.idle_right_index += 1

            if animations.idle_right_index >= len(animations.idle_right_images):
                animations.idle_right_index = 0
            
            self.image = animations.idle_right_images[animations.idle_right_index]
        self.image = pygame.transform.scale(self.image, (172, 172))

    def wizardFirebomb(self):
        if instantiate.direction == "left":
            animations.wizard_bomb_left_index += 1

            if animations.wizard_bomb_left_index >= len(animations.wizard_bomb_left_images):
                animations.wizard_bomb_left_index = 0
        
            self.image = animations.wizard_bomb_left_images[animations.wizard_bomb_left_index]
        else:
            animations.wizard_bomb_right_index += 1

            if animations.wizard_bomb_right_index >= len(animations.wizard_bomb_right_images):
                animations.wizard_bomb_right_index = 0
        
            self.image = animations.wizard_bomb_right_images[animations.wizard_bomb_right_index]
        self.image = pygame.transform.scale(self.image, (172, 172))
    
    def wizardThunder(self):
        if instantiate.direction == "left":
            animations.wizard_thunder_left_index += 1

            if animations.wizard_thunder_left_index >= len(animations.wizard_thunder_left_images):
                animations.wizard_thunder_left_index = 0
        
            self.image = animations.wizard_thunder_left_images[animations.wizard_thunder_left_index]
        else:
            animations.wizard_thunder_right_index += 1

            if animations.wizard_thunder_right_index >= len(animations.wizard_thunder_right_images):
                animations.wizard_thunder_right_index = 0
        
            self.image = animations.wizard_thunder_right_images[animations.wizard_thunder_right_index]
        self.image = pygame.transform.scale(self.image, (172, 172))
    
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if animations.attacking == "false" and gui_open == "false":
            if pressed_keys[pygame.K_LEFT]:
                self.moveLeft(savedata.speed1)
            else:
                if pressed_keys[pygame.K_RIGHT]:
                    self.moveRight(savedata.speed1)
                else:
                    if pressed_keys[pygame.K_DOWN]:
                        self.moveForward(savedata.speed2)
                    else:
                        if pressed_keys[pygame.K_UP]:
                            self.moveBack(savedata.speed2)
                        else:
                            self.idle()

class House(pygame.sprite.Sprite):
    def __init__(self, width, height, rotation):
        super().__init__()

        self.image = pygame.image.load("house/House.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image = pygame.transform.rotate(self.image, rotation)

        self.rect = self.image.get_rect()
        screen.blit(self.image, self.rect)

class Tree(pygame.sprite.Sprite):
    def __init__(self, type, width, height, rotation):
        super().__init__()

        if type == 1:
            self.image = pygame.image.load("tree/TallTree.png")
        else:
            self.image = pygame.image.load("tree/ThickTree.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image = pygame.transform.rotate(self.image, rotation)

        self.rect = self.image.get_rect()
        screen.blit(self.image, self.rect)

class SpellObjects(pygame.sprite.Sprite):
    def __init__(self, spell):
        super().__init__()
        if spell == "fire":
            self.image = pygame.image.load("menu/Firebomb.png")
            self.image = pygame.transform.scale(self.image, (64, 64))
            self.rect = self.image.get_rect()
            screen.blit(self.image, self.rect)
        
        if spell == "thunder":
            self.image = pygame.image.load("menu/Firebomb.png")
            self.image = pygame.transform.scale(self.image, (64, 64))
            self.rect = self.image.get_rect()
            screen.blit(self.image, self.rect)
    
    def gain_spell(self):
        self.kill()

class SpellGlow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # animations.glow_index = 0
        self.image = animations.glow_images[animations.glow_index]
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        screen.blit(self.image, self.rect)
    
    def gain_spell(self):
        self.kill()
    
    def update(self):
        animations.glow_index += 1

        if animations.glow_index >= len(animations.glow_images):
            animations.glow_index = 0
            
        self.image = animations.glow_images[animations.glow_index]
        self.image = pygame.transform.scale(self.image, (64, 64))

class Slime(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        
        self.image = animations.slime_idle_images[animations.slime_idle_index]
        self.image = pygame.transform.scale(self.image, (89, 89))
        self.rect = self.image.get_rect()
        screen.blit(self.image, self.rect)
    
    def hurt(self):
        self.health -= 2
        # print(self.health)
        
        animations.slime_hurt_index += 1
        
        if animations.slime_hurt_index >= len(animations.slime_hurt_images):
            animations.slime_hurt_index = 0
        
        self.image = animations.slime_hurt_images[animations.slime_hurt_index]
        self.image = pygame.transform.scale(self.image, (89, 89))
        
        damage_font = pygame.font.Font("fonts/PixelFont.ttf", 16)
        damage_text = damage_font.render("2", True, green)
        screen.blit(damage_text, (self.rect.x / 2, self.rect.y / 2))
        
        if self.health == 0:
            slimeball = Item(1)
            slimeball.rect.x = self.rect.x
            slimeball.rect.y = self.rect.y
            item_sprite_list.add(slimeball)
            self.kill()
    
    def idle(self):
        animations.slime_idle_index += 1
        
        if animations.slime_idle_index >= len(animations.slime_idle_images):
            animations.slime_idle_index = 0
        
        self.image = animations.slime_idle_images[animations.slime_idle_index]
        self.image = pygame.transform.scale(self.image, (89, 89))
    
    def update(self):
        if animations.attacking != "false" and pygame.sprite.spritecollideany(main_character, enemy_sprite_list):
            self.hurt()
        else:
            self.idle()

class Item(pygame.sprite.Sprite):
    def __init__(self, item_number):
        super().__init__()
        
        if item_number == 1:
            self.image = pygame.image.load("items/slimeball.png")
            self.image = pygame.transform.scale(self.image, (21, 21))
        
        self.rect = self.image.get_rect()
        screen.blit(self.image, self.rect)

class NewSprite(pygame.sprite.Sprite):
    def __init__(self, surface_color, color, height, width, border_radius):
        super().__init__()
  
        self.image = pygame.Surface([width, height])
        self.image.fill(surface_color)
        self.image.set_colorkey(color)
  
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height), width, border_radius)
  
        self.rect = self.image.get_rect()
    
    def remove(self):
        self.kill()

main_character = MainCharacter()
main_character.rect.x = width / 2 - 86
main_character.rect.y = height / 2 - 86

spell_object1 = SpellObjects("fire")
spell_glow1 = SpellGlow()

def stage_one():
    map.paths("y")
    
def stage_two():
    spell_gain = 0
    if spell_gain == 0 and 375 > main_character.rect.x > 335 and 180 > main_character.rect.y > 140:
        spell_object1.gain_spell()
        spell_glow1.gain_spell()
        spell_gain = 1
        savedata.fireball_spell = 1
        if savedata.spell_slot1 == "empty":
            savedata.spell_slot1 = "fireball"
        else:
            if savedata.spell_slot1 != "fireball" and savedata.spell_slot3 != "fireball" and savedata.spell_slot2 == "empty":
                savedata.spell_slot2 = "fireball"
            else:
                if savedata.spell_slot2 != "fireball" and savedata.spell_slot1 != "fireball" and savedata.spell_slot3 == "empty":
                    savedata.spell_slot3 = "fireball"

def check_attacks():
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if animations.attacking == "false" and 350 <= mouse[0] <= 398 and 428 <= mouse[1] <= 476:
                # animations.attacking = "true"
                if savedata.spell_slot1 == "fireball":
                    animations.attacking = "fireball"
                    animations.wizard_bomb_left_index = 0
                    animations.wizard_bomb_right_index = 0
                if savedata.spell_slot1 == "thunder":
                    animations.attacking = "thunder"
                    animations.wizard_thunder_left_index = 0
                    animations.wizard_thunder_right_index = 0
        
        if animations.attacking == "false" and 402 <= mouse[0] <= 450 and 428 <= mouse[1] <= 476:
                # animations.attacking = "true"
                if savedata.spell_slot2 == "fireball":
                    animations.attacking = "fireball"
                    animations.wizard_bomb_left_index = 0
                    animations.wizard_bomb_right_index = 0
                if savedata.spell_slot2 == "thunder":
                    animations.attacking = "thunder"
                    animations.wizard_thunder_left_index = 0
                    animations.wizard_thunder_right_index = 0
        
        if animations.attacking == "false" and 454 <= mouse[0] <= 502 and 428 <= mouse[1] <= 476:
                # animations.attacking = "true"
                if savedata.spell_slot3 == "fireball":
                    animations.attacking = "fireball"
                    animations.wizard_bomb_left_index = 0
                    animations.wizard_bomb_right_index = 0
                if savedata.spell_slot3 == "thunder":
                    animations.attacking = "thunder"
                    animations.wizard_thunder_left_index = 0
                    animations.wizard_thunder_right_index = 0

    if animations.attacking == "fireball":
        main_character.wizardFirebomb()
    if animations.attacking == "thunder":
        main_character.wizardThunder()
    
    if animations.wizard_bomb_right_index == 323 or animations.wizard_bomb_left_index == 323 or animations.wizard_thunder_right_index == 348 or animations.wizard_thunder_left_index == 348:
        animations.attacking = "false"

def ui_buttons():
    global gui_open
    global tab
    mouse = pygame.mouse.get_pos()
    
    if gui_open == "false" and 108 <= mouse[0] <= 156 and height - 52 <= mouse[1] <= height - 4:
        gui_open = "spellbook"

    if gui_open == "false" and 64 <= mouse[0] <= 102 and height - 52 <= mouse[1] <= height - 4:
        gui_open = "inventory"
        tab = "backpack"
                    
    if gui_open == "spellbook" and 460 <= mouse[0] <= 600 and 42 <= mouse[1] <= 80:
        gui_open = "false"
                    
    if gui_open == "inventory" and 460 <= mouse[0] <= 600 and 42 <= mouse[1] <= 80:
        gui_open = "false"
