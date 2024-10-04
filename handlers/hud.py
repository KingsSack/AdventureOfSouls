import pygame

from classes.hud.button import Button
from classes.spritesheet import Spritesheet


class HUD:
    def __init__(self, screen, savedata, player):
        self.screen = screen
        self.savedata = savedata
        self.player = player

        self.button_size = 48
        self.gap = 8

        self.menu_buttons = self.load_buttons()

    def load_buttons(self):
        spritesheet = Spritesheet("assets/ui/MenusIcons_34x34.png")
        button_data = [["settings_icon", self.player.inventory],
                       ["map_icon", self.player.inventory],
                       ["inventory_icon", self.player.inventory]]

        buttons = [
            Button(
                self.screen,
                (i + 1) * self.gap + i * self.button_size,
                self.screen.get_height() - (self.gap + self.button_size),
                self.button_size,
                spritesheet.parse_sprite(data[0]),
                data[1]
            )
            for i, data in enumerate(button_data)
        ]

        return buttons

    def update_window_size(self, height):
        for i, button in enumerate(self.menu_buttons):
            button.update_position(
                (i + 1) * self.gap + i * self.button_size,
                height - (self.gap + self.button_size)
            )

    def draw(self):
        for button in self.menu_buttons:
            button.draw()

        if self.player.inventory.is_open:
            self.player.inventory.draw()

    def update(self, mouse, events):
        for event in events:
            if event.type == pygame.VIDEORESIZE:
                self.update_window_size(event.h)

        for button in self.menu_buttons:
            if button.update(mouse, events):
                button.trigger_action()

        self.player.inventory.update()
