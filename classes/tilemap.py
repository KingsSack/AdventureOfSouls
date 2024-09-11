import pygame

from classes.tile import EmptyTile, Tile


class Tilemap():
    def __init__(self, spritesheet, map, window_width, window_height):
        self.map = map
        self.spritesheet = spritesheet
        self.window_width = window_width
        self.window_height = window_height
        self.tile_size = self.calculate_tile_size()
        self.tiles = self.load_tiles(map)
        self.map_surface = pygame.Surface((window_width, window_height))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()

    def calculate_tile_size(self):
        rows = len(self.map)
        cols = len(self.map[0]) if rows > 0 else 0
        tile_width = self.window_width // cols
        tile_height = self.window_height // rows
        return min(tile_width, tile_height)
    
    def update_window_size(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.tile_size = self.calculate_tile_size()
        self.map_surface = pygame.Surface((window_width, window_height))
        self.map_surface.set_colorkey((0, 0, 0))
        self.tiles = self.load_tiles(self.map)
        self.load_map()

    def draw_map(self, screen):
        map_width = len(self.map[0]) * self.tile_size
        map_height = len(self.map) * self.tile_size
        offset_x = (self.window_width - map_width) // 2
        offset_y = (self.window_height - map_height) // 2
        screen.blit(self.map_surface, (offset_x, offset_y))

    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)

    def load_tiles(self, map):
        tiles = []
        x, y = 0, 0
        for row in map:
            x = 0
            for tile in row:
                if tile != '':
                    tiles.append(Tile(tile, x * self.tile_size, y * self.tile_size, self.spritesheet, self.tile_size))
                else:
                    tiles.append(EmptyTile())
                x += 1
            y += 1
        return tiles
