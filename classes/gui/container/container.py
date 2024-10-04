import pygame

from classes.gui.gui import GUI
from classes.item.item import Item


class Container(GUI):
    def __init__(self, screen, title, num_slots: tuple, contents=[], gap=6):
        width = 96 + num_slots[0] * (48 + gap)
        height = 96 + num_slots[1] * (48 + gap)

        super().__init__(screen, title, screen.get_width() / 2 - width / 2,
                         screen.get_height() / 2 - height / 2, width, height)
        self.slot = pygame.transform.scale(
            pygame.image.load("assets/ui/ItemBox_24x24.png"), (48, 48))

        self.num_rows, self.num_cols = num_slots
        self.contents = contents
        self.gap = gap

    def add_item(self, item: Item):
        self.contents.append(item)

    def draw(self):
        super().draw()

        for row_num in range(self.num_rows):
            for col_num in range(self.num_cols):
                self.screen.blit(self.slot,
                                 (self.x + 48 + col_num * (48 + self.gap),
                                  self.y + 48 + row_num * (48 + self.gap)))

        for i, item in enumerate(self.contents):
            row_num = i // self.num_cols
            col_num = i % self.num_cols
            self.screen.blit(item.icon,
                             (self.x + 48 + col_num * (48 + self.gap),
                              self.y + 48 + row_num * (48 + self.gap)))
