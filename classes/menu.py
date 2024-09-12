import pygame
import fonts

from classes.button import Button


class Menu:
    def __init__(self, screen, in_menu=True):
        self.screen = screen
        self.in_menu = in_menu
        
        self.background_color = (50, 255, 100)
        self.foreground_color = (0, 0, 0)
        self.text_color = (0, 255, 0)
        
        self.play_button = Button(self.screen, fonts.primary_font, "Play", self.text_color, self.foreground_color, self.screen.get_width() / 2 - 50, self.screen.get_height() / 2 - 23, 100, 46)

    def draw(self):
        self.screen.fill(self.background_color)
        self.play_button.draw()

    def update(self, mouse, events):
        for event in events:
            if event.type == pygame.VIDEORESIZE:
                self.play_button.resize(self.screen.get_width() / 2 - 50, self.screen.get_height() / 2 - 23, 100, 46)
        self.in_menu = not self.play_button.update(mouse, events)
