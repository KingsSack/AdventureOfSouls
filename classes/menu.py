import sys
import pygame
import fonts


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = self.screen.get_size()
        self.in_menu = True
        self.background = (50, 255, 100)
        self.foreground = (0, 0, 0)
        self.text = (0, 255, 0)
        self.play_text = fonts.primary_font.render("Play", True, self.text)

    def update(self, mouse, events):
        self.width, self.height = self.screen.get_size()
        self.check_input(mouse, events)

    def draw(self):
        self.screen.fill(self.background)

        pygame.draw.rect(self.screen, self.foreground, [self.width / 2 - 50, self.height / 2 - 23, 100, 46], 0, 4)
        self.screen.blit(self.play_text, (self.width / 2 - 34, self.height / 2 - 9))

    def check_input(self, mouse, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.width / 2 - 50 <= mouse[0] <= self.width / 2 + 50 and self.height / 2 - 23 <= mouse[1] <= self.height / 2 + 23:
                        self.in_menu = False
