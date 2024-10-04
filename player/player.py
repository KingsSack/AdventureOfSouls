from enum import Enum

import pygame

from classes.collider import Collider
from classes.entity.entity import Entity
from classes.gui.container.inventory import Inventory
from classes.item.cloak.cloak import Cloak
from classes.item.weapon.weapon import Weapon


class PlayerState(Enum):
    ADVENTURE = 1
    COMBAT = 2
    DIALOGUE = 3


class Player(Entity):
    def __init__(self, screen, savedata):
        super().__init__(
            screen,
            x=(screen.get_width() / 2) - 64,
            y=(screen.get_height() / 2) - 96,
            width=128,
            height=128,
            hitbox=Collider(self, 48, 36, 48, 64),
            idle_animation="player_idle",
            walk_animation="player_walk",
        )
        self.savedata = savedata

        self.health = self.savedata.get_or_set_default("health", 100)
        self.inventory = Inventory(self.screen, self.savedata)

        self.cloak = self.savedata.get_or_set_default("cloak", None)
        self.weapon = self.savedata.get_or_set_default("weapon", None)

        self.spells = self.savedata.get_or_set_default("spells", [])

        self.state = PlayerState.ADVENTURE

    def equip_cloak(self, cloak: Cloak):
        self.cloak = cloak
        self.change_animations(self.cloak.idle_animation,
                               self.cloak.walk_animation)

    def equip_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def calculate_power(self) -> int:
        power = 5
        if self.cloak:
            power += self.cloak.power_modifier
        if self.weapon:
            power += self.weapon.power_modifier
        return power

    def calculate_defense(self) -> int:
        defense = 5
        if self.cloak:
            defense += self.cloak.defense_modifier
        if self.weapon:
            defense += self.weapon.defense_modifier
        return defense

    def calculate_speed(self) -> int:
        speed = 5
        if self.cloak:
            speed += self.cloak.speed_modifier
        if self.weapon:
            speed += self.weapon.speed_modifier
        return speed

    def initiate_combat(self, opponent):
        self.state = PlayerState.COMBAT

    def initiate_dialogue(self, npc):
        self.state = PlayerState.DIALOGUE

    def attack(self, opponent):
        damage = self.calculate_power() - opponent.calculate_defense()
        opponent.health -= damage

    def move(self, pressed_keys):
        if (
            pressed_keys[pygame.K_w]
            or pressed_keys[pygame.K_UP]
            or pressed_keys[pygame.K_s]
            or pressed_keys[pygame.K_DOWN]
            or pressed_keys[pygame.K_a]
            or pressed_keys[pygame.K_LEFT]
            or pressed_keys[pygame.K_d]
            or pressed_keys[pygame.K_RIGHT]
        ):
            self.moving = True
        else:
            self.moving = False

        if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
            self.y -= self.calculate_speed()
        if pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
            self.y += self.calculate_speed()
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            self.flip = True
            self.x -= self.calculate_speed()
        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            self.flip = False
            self.x += self.calculate_speed()

    def update(self, pressed_keys):
        super().update()
        self.move(pressed_keys)
