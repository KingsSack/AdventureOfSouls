import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, icon):
        super().__init__()
        self.screen = screen

        self.x, self.y = x, y

        self.icon = icon
        self.icon_rect = self.icon.get_rect()

    def draw(self):
        self.screen.blit(self.icon, self.icon_rect)

    def update(self, mouse, events):
        mouse_x, mouse_y = mouse
        if self.icon_rect.collidepoint(mouse_x, mouse_y):
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    return True
        return False
