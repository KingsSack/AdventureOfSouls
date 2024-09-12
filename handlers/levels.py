import json
import pygame

from classes.level import Level
from classes.spritesheet import Spritesheet
from classes.tilemap import Tilemap
from entities.chicken import Chicken


class Levels:
    def __init__(self, screen, savedata, player):
        self.screen = screen
        self.savedata = savedata
        self.player = player
        self.current_level = savedata.data.get('current_level', 'ardale_lower')
        self.level = None
        
        self.grass_spritesheet = Spritesheet('assets/tilesets/Grass.png')
        self.path_spritesheet = Spritesheet('assets/tilesets/Tilled_Dirt_v2.png')
        self.layer_1 = []
        self.layer_2 = []
        self.entities = []

        self.load_level(self.current_level)
    
    def load_tilemaps(self):
        try:
            self.layer_1 = Tilemap(self.grass_spritesheet, self.level.layer_1, self.screen.get_width(), self.screen.get_height())
            self.layer_2 = Tilemap(self.path_spritesheet, self.level.layer_2, self.screen.get_width(), self.screen.get_height())
        except:
            print("Layers are not formatted correctly.")

    def load_entities(self):
        self.entities.clear()
        try:
            [self.entities.append(Chicken(self.screen, x, y)) for x, y in self.level.entities["chickens"]]
        except KeyError as e:
            print(f"KeyError: {e} - Entity names might be mispelled or not in expected format.")
        except TypeError as e:
            print(f"TypeError: {e} - Entities might not be iterable or not in expected format.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def load_level(self, name):
        try:
            with open(f'data/levels/{name}.json', 'r') as file:
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
        self.savedata.modify_data('current_level', self.current_level)

    def check_level(self):
        if self.player.rect.x < 0:
            self.load_level(self.level.surrounding_levels['left'])
            self.player.rect.x = self.screen.get_width() - 128
        elif self.player.rect.y < 0:
            self.load_level(self.level.surrounding_levels['above'])
            self.player.rect.y = self.screen.get_height() - 128
        elif self.player.rect.x > self.screen.get_width():
            self.load_level(self.level.surrounding_levels['right'])
            self.player.rect.x = 0
        elif self.player.rect.y > self.screen.get_height():
            self.load_level(self.level.surrounding_levels['below'])
            self.player.rect.y = 0
    
    def update_level(self):
        [entity.update() for entity in self.entities]

    def draw_level(self):
        self.screen.fill(self.level.background_color)
        
        self.layer_1.draw_map(self.screen)
        self.layer_2.draw_map(self.screen)
        
        [entity.draw() for entity in self.entities]

    def update(self, events):
        for event in events:
            if event.type == pygame.VIDEORESIZE:
                self.layer_1.update_window_size(event.w, event.h)
                self.layer_2.update_window_size(event.w, event.h)
        
        self.check_level()
        self.update_level()
        self.draw_level()
