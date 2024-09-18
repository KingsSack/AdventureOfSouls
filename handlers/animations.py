import json
import time
import pygame

from classes.animation import Animation
from classes.spritesheet import Spritesheet


class Animations:
    def __init__(self, animation_name):
        self.current_animation = animation_name
        self.animation = None

        self.load_animation(self.current_animation)

        self.timestamp = time.time()

    def load_animation(self, name):
        with open(f"data/animations/{name}.json", "r", encoding="utf-8") as file:
            self.current_animation = name

            animation_data = json.load(file)

            try:
                self.animation = Animation(**animation_data)
            except (TypeError, ValueError) as e:
                print(f"Error: {e} - Animation data is not formatted correctly.")
                return

        spritesheet = Spritesheet(f"assets/{self.animation.path}.png")
        for i in range(self.animation.num_frames):
            self.animation.frames.append(
                spritesheet.parse_sprite(f"{self.animation.name}{i + 1}")
            )

    def get_frame(self) -> pygame.Surface:
        if time.time() - self.timestamp >= 1 / self.animation.fps:
            self.animation.index += 1
            self.timestamp = time.time()

        if self.animation.index >= self.animation.num_frames:
            self.animation.index = 0

        return self.animation.frames[self.animation.index]
