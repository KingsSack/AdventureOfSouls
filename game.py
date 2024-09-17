from classes.menu import Menu
from handlers.levels import Levels
from handlers.savedata import Data
from player.player import Player


class GameManager:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.debug = False
        self.savedata = Data()
        self.main_menu = Menu(self.screen)
        self.player = Player(self.screen, self.savedata)
        self.level_handler = Levels(self.screen, self.savedata, self.player)

    def update(self, mouse, events, pressed_keys):
        if self.main_menu.in_menu:
            self.main_menu.update(mouse, events)
            self.main_menu.draw()
        elif self.player.in_combat:
            pass
        else:
            self.level_handler.update(self.debug, events)
            self.player.update(pressed_keys)
            self.player.draw(self.debug)
