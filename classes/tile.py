import pygame


class EmptyTile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def draw(self, screen):
        pass

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, spritesheet, tile_size):
        super().__init__()
        image = spritesheet.parse_sprite(image)
        self.sprite = pygame.transform.scale(image, (tile_size, tile_size))
        self.rect = self.sprite.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)
