import json
import pygame

from classes.level import Level
from classes.spritesheet import Spritesheet
from classes.tilemap import Tilemap
from entities.chicken import Chicken
from entities.golem import Golem
from entities.wizard import Wizard


class Levels:
    def __init__(self, screen, savedata, player):
        self.screen = screen
        self.savedata = savedata
        self.player = player
        self.current_level = savedata.data.get("current_level", "ardale_lower")
        self.level = None

        self.grass_spritesheet = Spritesheet("assets/tilesets/Grass.png")
        self.path_spritesheet = Spritesheet("assets/tilesets/Tilled_Dirt_v2.png")
        self.layer_1 = None
        self.layer_2 = None
        self.entities = []
        self.enemies = []
        self.npcs = []

        self.load_level(self.current_level)

    def load_tilemaps(self):
        try:
            self.layer_1 = Tilemap(
                self.grass_spritesheet,
                self.level.layer_1,
                self.screen.get_width(),
                self.screen.get_height(),
            )
            self.layer_2 = Tilemap(
                self.path_spritesheet,
                self.level.layer_2,
                self.screen.get_width(),
                self.screen.get_height(),
            )
        except (AttributeError, TypeError, ValueError) as e:
            print(f"Error loading tilemaps: {e}")

    def load_entities(self):
        self.entities.clear()
        try:
            [
                self.entities.append(Chicken(self.screen, x, y))
                for x, y in self.level.entities["chickens"]
            ]
        except KeyError as e:
            print(
                f"KeyError: {e} - Entity names might be mispelled or not in expected format."
            )
        except TypeError as e:
            print(
                f"TypeError: {e} - Entities might not be iterable or not in expected format."
            )
        except AttributeError as e:
            print(f"AttributeError: {e} - Level data might be missing.")

    def load_enemies(self):
        self.enemies.clear()
        try:
            [
                self.enemies.append(Golem(self.screen, self.player, x, y))
                for x, y in self.level.enemies["golems"]
            ]
        except KeyError as e:
            print(
                f"KeyError: {e} - Enemy names might be mispelled or not in expected format."
            )
        except TypeError as e:
            print(
                f"TypeError: {e} - Enemies might not be iterable or not in expected format."
            )
        except AttributeError as e:
            print(f"AttributeError: {e} - Level data might be missing.")
    
    def load_npcs(self):
        self.npcs.clear()
        try:
            self.npcs.append(Wizard(self.screen, self.player, self.level.npcs["wizard"][0], self.level.npcs["wizard"][1]))
        except KeyError as e:
            print(
                f"KeyError: {e} - NPC names might be mispelled or not in expected format."
            )
        except TypeError as e:
            print(
                f"TypeError: {e} - NPC might not be iterable or not in expected format."
            )
        except AttributeError as e:
            print(f"AttributeError: {e} - Level data might be missing.")

    def load_level(self, name):
        try:
            with open(f"data/levels/{name}.json", "r", encoding="utf-8") as file:
                level_data = json.load(file)
        except FileNotFoundError:
            print(f"Level file '{name}.json' does not exist.")
            return
        except json.JSONDecodeError:
            print(f"Level file '{name}.json' is not a valid JSON.")
            return

        try:
            self.level = Level(**level_data)
        except TypeError:
            print("Level data is not formatted correctly.")
            return

        self.current_level = name
        self.load_tilemaps()
        self.load_entities()
        self.load_enemies()
        self.load_npcs()
        self.savedata.modify_data("current_level", self.current_level)

    def check_level(self):
        if self.player.x < 0:
            self.load_level(self.level.surrounding_levels["left"])
            self.player.x = self.screen.get_width() - 128
        elif self.player.y < 0:
            self.load_level(self.level.surrounding_levels["above"])
            self.player.y = self.screen.get_height() - 128
        elif self.player.x > self.screen.get_width():
            self.load_level(self.level.surrounding_levels["right"])
            self.player.x = 0
        elif self.player.y > self.screen.get_height():
            self.load_level(self.level.surrounding_levels["below"])
            self.player.y = 0

        for enemy in self.enemies:
            if self.player.hitbox.collides(enemy.hitbox):
                self.player.initiate_combat(enemy)
                return
        
        for npc in self.npcs:
            if self.player.hitbox.collides(npc.hitbox):
                self.player.initiate_dialogue(npc)
                return

    def update_level(self):
        for entity in self.entities:
            entity.update()
        for enemy in self.enemies:
            enemy.update()
        for npc in self.npcs:
            npc.update()

    def draw_level(self, debug):
        self.screen.fill(self.level.background_color)

        self.layer_1.draw_map(self.screen)
        self.layer_2.draw_map(self.screen)

        for entity in self.entities:
            entity.draw(debug)
        for enemy in self.enemies:
            enemy.draw(debug)
        for npc in self.npcs:
            npc.draw(debug)

    def update(self, debug, events):
        for event in events:
            if event.type == pygame.VIDEORESIZE:
                self.layer_1.update_window_size(event.w, event.h)
                self.layer_2.update_window_size(event.w, event.h)

        self.update_level()
        self.check_level()
        self.draw_level(debug)
