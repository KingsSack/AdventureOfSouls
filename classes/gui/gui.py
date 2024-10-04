import pygame

import fonts


class GUI(pygame.sprite.Sprite):
    def __init__(self, screen, title, x, y, width, height):
        self.is_open = False

        self.screen = screen

        self.title = title

        self.x, self.y = x, y
        self.width, self.height = width, height

        self.sprite = pygame.transform.scale(pygame.image.load(
            "assets/ui/RectangleBox_96x96.png"), (self.width, self.height))
        self.title = fonts.primary_font.render(self.title,
                                               True, (186, 145, 88))
        self.title_background = pygame.transform.scale(pygame.image.load("assets/ui/TitleBox_64x16.png"),
                                                       (self.title.get_width() + 32, (self.title.get_width() + 32) / 4))

        self.rect = self.sprite.get_rect()
        self.rect.x, self.rect.y = self.x, self.y

    def toggle(self):
        self.is_open = not self.is_open

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))
        self.screen.blit(self.title_background, (self.x + (self.width / 2 - (self.title_background.get_width() / 2)),
                                                 self.y - 11))
        self.screen.blit(self.title, (self.x + (self.width / 2 - (self.title.get_width() / 2)),
                                      (self.y - 11) + 12))

    def update(self):
        pass
