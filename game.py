import instantiate
import time
import pygame
import animations
import map
import savedata
import collisions

current_stage = "menu"

size = width, height = 852, 480
screen = pygame.display.set_mode(size)

RED = 255, 25, 25
GREEN = 25, 255, 25

map_sprites = pygame.sprite.Group()

level_sprites_list = pygame.sprite.Group()
tutorial_sprites_list = pygame.sprite.Group()
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

        self.health = 1000
        self.direction = "right"
        
        self.timestamp = time.time()
        
        if animations.attacking == "false":
            if self.direction == "left":
                self.image = animations.idle_left_images[animations.idle_left_index]
                self.image = pygame.transform.scale(self.image, (172, 172))
            else:
                self.image = animations.idle_right_images[animations.idle_right_index]
                self.image = pygame.transform.scale(self.image, (172, 172))

        self.rect = self.image.get_rect()
        
        screen.blit(self.image, self.rect)
    
    def moveRight(self, pixels):
        self.rect.x += pixels
        
        self.direction = "right"
        
        if time.time() - self.timestamp >= 1 / animations.walk_right_fps:
            animations.walk_right_index += 1
            self.timestamp = time.time()
        
        if animations.walk_right_index >= len(animations.walk_right_images):
            animations.walk_right_index = 0
        
        self.image = animations.walk_right_images[animations.walk_right_index]
        self.image = pygame.transform.scale(self.image, (172, 172))
    
    def moveLeft(self, pixels):
        self.rect.x -= pixels
        
        self.direction = "left"
        
        if time.time() - self.timestamp >= 1 / animations.walk_left_fps:
            animations.walk_left_index += 1
            self.timestamp = time.time()
        
        if animations.walk_left_index >= len(animations.walk_left_images):
            animations.walk_left_index = 0
        
        self.image = animations.walk_left_images[animations.walk_left_index]
        self.image = pygame.transform.scale(self.image, (172, 172))
    
    def moveForward(self, speed):
        self.rect.y += speed * speed / 10

        if self.direction == "left":
            if time.time() - self.timestamp >= 1 / animations.walk_left_fps:
                animations.walk_left_index += 1
                self.timestamp = time.time()
            
            if animations.walk_left_index >= len(animations.walk_left_images):
                animations.walk_left_index = 0
            
            self.image = animations.walk_left_images[animations.walk_left_index]
        else:
            if time.time() - self.timestamp >= 1 / animations.walk_right_fps:
                animations.walk_right_index += 1
                self.timestamp = time.time()
            
            if animations.walk_right_index >= len(animations.walk_right_images):
                animations.walk_right_index = 0
            
            self.image = animations.walk_right_images[animations.walk_right_index]
        self.image = pygame.transform.scale(self.image, (172, 172))
    
    def moveBack(self, speed):
        self.rect.y -= speed * speed / 10

        if self.direction == "left":
            if time.time() - self.timestamp >= 1 / animations.walk_left_fps:
                animations.walk_left_index += 1
                self.timestamp = time.time()
            
            if animations.walk_left_index >= len(animations.walk_left_images):
                animations.walk_left_index = 0
            
            self.image = animations.walk_left_images[animations.walk_left_index]
        else:
            if time.time() - self.timestamp >= 1 / animations.walk_right_fps:
                animations.walk_right_index += 1
                self.timestamp = time.time()
            
            if animations.walk_right_index >= len(animations.walk_right_images):
                animations.walk_right_index = 0
            
            self.image = animations.walk_right_images[animations.walk_right_index]
        self.image = pygame.transform.scale(self.image, (172, 172))
    
    def idle(self):
        if self.health > 0:
            if self.direction == "left":
                if time.time() - self.timestamp >= 1 / animations.idle_left_fps:
                    animations.idle_left_index += 1
                    self.timestamp = time.time()
                
                if animations.idle_left_index >= len(animations.idle_left_images):
                    animations.idle_left_index = 0
                    
                self.image = animations.idle_left_images[animations.idle_left_index]
            else:
                if time.time() - self.timestamp >= 1 / animations.idle_right_fps:
                    animations.idle_right_index += 1
                    self.timestamp = time.time()
                
                if animations.idle_right_index >= len(animations.idle_right_images):
                    animations.idle_right_index = 0
                
                self.image = animations.idle_right_images[animations.idle_right_index]
            self.image = pygame.transform.scale(self.image, (172, 172))
    
    def hurt(self, damage):
        if self.health > 0:
            if self.direction == "left":
                if time.time() - self.timestamp >= 1 / animations.hurt_left_fps:
                    animations.hurt_left_index += 1
                    self.timestamp = time.time()
                
                if animations.hurt_left_index >= len(animations.hurt_left_images):
                    animations.hurt_left_index = 0
                    
                self.image = animations.hurt_left_images[animations.hurt_left_index]
            else:
                if time.time() - self.timestamp >= 1 / animations.hurt_right_fps:
                    animations.hurt_right_index += 1
                    self.timestamp = time.time()
                
                if animations.hurt_right_index >= len(animations.hurt_right_images):
                    animations.hurt_right_index = 0
                    
                self.image = animations.hurt_right_images[animations.hurt_right_index]
            self.image = pygame.transform.scale(self.image, (172, 172))
            
            self.health -= damage

    def wizardFirebomb(self):
        if self.health > 0:
            if self.direction == "left":
                if time.time() - self.timestamp >= 1 / animations.wizard_bomb_left_fps:
                    animations.wizard_bomb_left_index += 1
                    self.timestamp = time.time()
                
                if animations.wizard_bomb_left_index >= len(animations.wizard_bomb_left_images):
                    animations.wizard_bomb_left_index = 0
                    
                self.image = animations.wizard_bomb_left_images[animations.wizard_bomb_left_index]
            else:
                if time.time() - self.timestamp >= 1 / animations.wizard_bomb_right_fps:
                    animations.wizard_bomb_right_index += 1
                    self.timestamp = time.time()
                
                if animations.wizard_bomb_right_index >= len(animations.wizard_bomb_right_images):
                    animations.wizard_bomb_right_index = 0
                    
                self.image = animations.wizard_bomb_right_images[animations.wizard_bomb_right_index]
            self.image = pygame.transform.scale(self.image, (172, 172))
    
    def wizardThunder(self):
        if self.health > 0:
            if self.direction == "left":
                if time.time() - self.timestamp >= 1 / animations.wizard_thunder_left_fps:
                    animations.wizard_thunder_left_index += 1
                    self.timestamp = time.time()
                
                if animations.wizard_thunder_left_index >= len(animations.wizard_thunder_left_images):
                    animations.wizard_thunder_left_index = 0
                    
                self.image = animations.wizard_thunder_left_images[animations.wizard_thunder_left_index]
            else:
                if time.time() - self.timestamp >= 1 / animations.wizard_thunder_right_fps:
                    animations.wizard_thunder_right_index += 1
                    self.timestamp = time.time()
                
                if animations.wizard_thunder_right_index >= len(animations.wizard_thunder_right_images):
                    animations.wizard_thunder_right_index = 0
                    
                self.image = animations.wizard_thunder_right_images[animations.wizard_thunder_right_index]
            self.image = pygame.transform.scale(self.image, (172, 172))
    
    def collect_item(self):
        for i in range(36):
            if savedata.inventory[i + 1] == "":
                item_sprite_list.update(i + 1)
                break
    
    def death(self):
        if self.direction == "left":
            if time.time() - self.timestamp >= 1 / animations.death_left_fps:
                    animations.death_left_index += 1
                    self.timestamp = time.time()
                
            if animations.death_left_index >= len(animations.death_left_images):
                animations.death_left_index = 0
                self.health = 1000
                self.rect.x = width / 2 - 86
                self.rect.y = height / 2 - 86
                    
            self.image = animations.death_left_images[animations.death_left_index]
        else:
            if time.time() - self.timestamp >= 1 / animations.death_right_fps:
                    animations.death_right_index += 1
                    self.timestamp = time.time()
                
            if animations.death_right_index >= len(animations.death_right_images):
                animations.death_right_index = 0
                self.health = 1000
                self.rect.x = width / 2 - 86
                self.rect.y = height / 2 - 86
                    
            self.image = animations.death_right_images[animations.death_right_index]
        self.image = pygame.transform.scale(self.image, (172, 172))
    
    def update(self):
        collisions.player_hitbox.update(self.rect.x + 64.5, self.rect.y + 40)
        
        health_ui.update(self.health)
        
        if self.health <= 0:
            self.death()
        else:
            pressed_keys = pygame.key.get_pressed()
            if animations.attacking == "false" and gui_open == "false":
                if pygame.sprite.spritecollideany(collisions.player_hitbox, item_sprite_list):
                    self.collect_item()
                
                if pressed_keys[pygame.K_LEFT]:
                    self.moveLeft(savedata.speed1)
                elif pressed_keys[pygame.K_RIGHT]:
                    self.moveRight(savedata.speed1)
                elif pressed_keys[pygame.K_DOWN]:
                    self.moveForward(savedata.speed2)
                elif pressed_keys[pygame.K_UP]:
                    self.moveBack(savedata.speed2)
                else:
                    self.idle()

class House(pygame.sprite.Sprite):
    def __init__(self, width, height, rotation):
        super().__init__()
        
        self.width, self.height = width, height

        self.image = pygame.image.load("house/House.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image = pygame.transform.rotate(self.image, rotation)
        
        self.rect = self.image.get_rect()
        
        # self.hitbox = [self.rect.x, self.rect.x + width, self.rect.y, self.rect.y + height - 60]
        
        screen.blit(self.image, self.rect)

class Tree(pygame.sprite.Sprite):
    def __init__(self, type, width, height, rotation):
        super().__init__()
        
        self.width, self.height = width, height
        
        if type == 1:
            self.image = pygame.image.load("tree/TallTree.png")
        else:
            self.image = pygame.image.load("tree/ThickTree.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image = pygame.transform.rotate(self.image, rotation)

        self.rect = self.image.get_rect()
        screen.blit(self.image, self.rect)

class Flower(pygame.sprite.Sprite):
    def __init__(self, type, width, height, rotation):
        super().__init__()
        
        self.width, self.height = width, height

        # if type == 1:
        #     self.image = pygame.image.load("tree/TallTree.png")
        # else:
        #     self.image = pygame.image.load("tree/ThickTree.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image = pygame.transform.rotate(self.image, rotation)

        self.rect = self.image.get_rect()
        screen.blit(self.image, self.rect)

class Rock(pygame.sprite.Sprite):
    def __init__(self, type, width, height, rotation):
        super().__init__()
        
        self.width, self.height = width, height

        if type == 1:
            self.image = pygame.image.load("vegetation/Rock1.png")
        else:
            self.image = pygame.image.load("vegetation/Rock1.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image = pygame.transform.rotate(self.image, rotation)

        self.rect = self.image.get_rect()
        screen.blit(self.image, self.rect)

class SpellObjects(pygame.sprite.Sprite):
    def __init__(self, spell):
        super().__init__()
        
        self.width, self.height = 64, 64
        
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
        self.health = 250
        self.direction = "right"
        
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
        
        damage_font = pygame.font.Font("fonts/PixelFont.ttf", 21)
        damage_text = damage_font.render("2", True, GREEN)
        screen.blit(damage_text, (self.rect.x + 40, self.rect.y + 40))
        
        if self.health == 0:
            slimeball = Item(1)
            slimeball.rect.x = self.rect.x + 42
            slimeball.rect.y = self.rect.y + 40
            item_sprite_list.add(slimeball)
            
            savedata.t = time.time()
            
            self.kill()
        
    def attack(self):
        animations.slime_jump_index += 1
        
        if animations.slime_jump_index >= len(animations.slime_jump_images):
            animations.slime_jump_index = 0
        
        self.image = animations.slime_jump_images[animations.slime_jump_index]
        self.image = pygame.transform.scale(self.image, (89, 89))
        
        main_character.hurt(1)
        
        if main_character.direction == "left":
            self.rect.x += 1
        else:
            self.rect.x -= 1
    
    def idle(self):
        animations.slime_idle_index += 1
        
        if animations.slime_idle_index >= len(animations.slime_idle_images):
            animations.slime_idle_index = 0
        
        self.image = animations.slime_idle_images[animations.slime_idle_index]
        self.image = pygame.transform.scale(self.image, (89, 89))
        
        if pygame.sprite.spritecollideany(main_character, enemy_sprite_list):
            if main_character.direction == "left":
                self.rect.x += 1
            else:
                self.rect.x -= 1
        else:
            if self.rect.x > width / 2 + 160:
                self.direction = "left"
            if self.rect.x < width / 2 - 160:
                self.direction = "right"
            
            if self.direction == "right":
                self.rect.x += 1
            else:
                self.rect.x -= 1
    
    def update(self):
        if pygame.sprite.spritecollideany(collisions.player_hitbox, enemy_sprite_list):
            if animations.attacking != "false":
                self.hurt()
            else:
                self.attack()
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
    
    def update(self, slot):
        if pygame.sprite.spritecollideany(collisions.player_hitbox, item_sprite_list):
            savedata.inventory[slot] = "slimeball"
            self.kill()

class Arrow(pygame.sprite.Sprite):
    def __init__(self, width, height, rotation, type):
        super().__init__()
        
        self.level = type
        
        self.frame = 0
        
        self.image = pygame.image.load("tutorial/arrow.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image = pygame.transform.rotate(self.image, rotation)
        
        self.rect = self.image.get_rect()
        
        screen.blit(self.image, self.rect)
    
    def update(self):
        self.frame += 1
        
        if self.frame >= 30:
            self.frame = 0
        
        if self.frame <= 15:
            self.rect.y = 36
        
        if self.frame > 15:
            self.rect.y = 46
        
        if savedata.tutorial_level > 2 and current_stage != "ardale_spawn":
            self.kill()

class TutorialBackdrop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        savedata.isbackdrop = True
        
        self.t = time.time()
        
        self.image = pygame.image.load("tutorial/TutorialBackdrop.png")
        self.image = pygame.transform.scale(self.image, (460, 160))
        
        self.rect = self.image.get_rect()
        
        screen.blit(self.image, self.rect)
    
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[pygame.K_SPACE] and time.time() - self.t > 6:
            savedata.tutorial_level += 1
            savedata.isbackdrop = False
            self.kill()
        
        screen.blit(self.image, self.rect)

class Sign(pygame.sprite.Sprite):
    def __init__(self, width, height, rotation, type):
        super().__init__()
        
        if type == "fire":
            self.image = pygame.image.load("signs/fire sign.png")
        elif type == "slime":
            self.image = pygame.image.load("signs/slime sign.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image = pygame.transform.rotate(self.image, rotation)
        
        self.rect = self.image.get_rect()
        
        screen.blit(self.image, self.rect)

class HealthUI(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.font = pygame.font.Font('fonts/UndertaleFont.ttf', 30)
        self.image = self.font.render("1000", True , RED)
        
        self.rect = self.image.get_rect()
    
    def update(self, health):
        self.image = self.font.render(f'{health}', True, RED)
        
        self.rect = self.image.get_rect()
        self.rect.x = 22
        self.rect.y = 28
        
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
character_sprite_list.add(main_character)

health_ui = HealthUI()
health_ui.rect.x = 5
health_ui.rect.y = 5

spell_object1 = SpellObjects("fire")
spell_glow1 = SpellGlow()

def ardale_spawn():
    map.paths("y")
    
def ardale_center():
    map.paths("spell1")
    
    # .spell_gain = 0
    if spell_object1.rect.colliderect(collisions.player_hitbox.rect):
        spell_object1.gain_spell()
        spell_glow1.gain_spell()
        # spell_gain = 1
        savedata.fireball_spell = 1
        if savedata.spell_slot1 == "empty":
            savedata.spell_slot1 = "fireball"
        elif savedata.spell_slot1 != "fireball" and savedata.spell_slot3 != "fireball" and savedata.spell_slot2 == "empty":
            savedata.spell_slot2 = "fireball"
        elif savedata.spell_slot2 != "fireball" and savedata.spell_slot1 != "fireball" and savedata.spell_slot3 == "empty":
            savedata.spell_slot3 = "fireball"

def ardale_countryside():
    map.paths("horizantal")

def flowerfield_entrance():
    map.paths("horizantal")


def check_attacks():
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if animations.attacking == "false" and 350 <= mouse[0] <= 398 and 428 <= mouse[1] <= 476:
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
    
    if animations.wizard_bomb_right_index == 26 or animations.wizard_bomb_left_index == 26 or animations.wizard_thunder_right_index == 348 or animations.wizard_thunder_left_index == 348:
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
