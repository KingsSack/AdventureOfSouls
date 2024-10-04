import pygame

from classes.gui.gui import GUI


class Button(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, size, icon, gui: GUI):
        super().__init__()
        self.screen = screen

        self.x, self.y = x, y
        self.size = size

        self.icon = pygame.transform.scale(icon, (self.size, self.size))
        self.sprite = pygame.transform.scale(pygame.image.load(
            "assets/ui/MenusBox_34x34.png"), (self.size, self.size))

        self.rect = self.sprite.get_rect()
        self.rect.x, self.rect.y = self.x, self.y

        self.gui = gui

    def update_position(self, x, y):
        self.x, self.y = x, y
        self.rect.x, self.rect.y = x, y

    def trigger_action(self):
        self.gui.toggle()

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))
        self.screen.blit(self.icon, (self.x, self.y))

    def update(self, mouse, events):
        mouse_x, mouse_y = mouse
        if self.rect.collidepoint(mouse_x, mouse_y):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    return True
        return False
