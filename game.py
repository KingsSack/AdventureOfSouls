from classes.menu.menu import Menu
from handlers.hud import HUD
from handlers.levels import Levels
from handlers.savedata import Data
from player.player import Player, PlayerState


class GameManager:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.debug = False
        self.savedata = Data()
        self.main_menu = Menu(self.screen)
        self.player = Player(self.screen, self.savedata)
        self.level_handler = Levels(self.screen, self.savedata, self.player)
        self.hud_handler = HUD(self.screen, self.savedata, self.player)

    def update(self, mouse, events, pressed_keys):
        if self.main_menu.in_menu:
            self.main_menu.update(mouse, events)
            self.main_menu.draw()
        elif self.player.state == PlayerState.COMBAT:
            pass
        elif self.player.state == PlayerState.DIALOGUE:
            pass
        elif self.player.state == PlayerState.ADVENTURE:
            self.level_handler.update(self.debug, events)
            self.player.update()
            self.player.move(pressed_keys)
            self.player.draw(self.debug)
            self.hud_handler.update(mouse, events)
            self.hud_handler.draw()
        else:
            print("Unknown player state, reverting to main menu.")
            self.main_menu.in_menu = True
            return
