import pygame

from handlers.animations import Animations


class Entity(pygame.sprite.Sprite):
    def __init__(
        self, screen, x, y, width, height, hitbox, idle_animation, walk_animation
    ):
        super().__init__()
        self.screen = screen

        self.moving = False
        self.flip = False

        self.x, self.y = x, y
        self.width, self.height = width, height

        self.hitbox = hitbox

        self.idle_animation = idle_animation
        self.walk_animation = walk_animation

        self.animation_handler = Animations(self.idle_animation)
        self.sprite = self.animation_handler.get_frame()

        self.rect = self.sprite.get_rect()
    
    def change_animations(self, idle_animation, walk_animation):
        self.idle_animation = idle_animation
        self.walk_animation = walk_animation

    def draw(self, debug):
        if (
            self.moving
            and self.animation_handler.current_animation != self.walk_animation
        ):
            self.animation_handler.load_animation(self.walk_animation)
        elif (
            not self.moving
            and self.animation_handler.current_animation == self.walk_animation
        ):
            self.animation_handler.load_animation(self.idle_animation)

        self.screen.blit(self.sprite, self.rect)

        if debug:
            pygame.draw.rect(self.screen, (255, 0, 0), self.hitbox.rect, 2)

    def update(self):
        self.rect.x, self.rect.y = self.x, self.y
        self.hitbox.update()
        self.sprite = pygame.transform.flip(
            pygame.transform.scale(
                self.animation_handler.get_frame(), (self.width, self.height)
            ),
            self.flip,
            False,
        )
