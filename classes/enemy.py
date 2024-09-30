import math

from classes.alert import Alert
from classes.entity import Entity


class Enemy(Entity):
    def __init__(
        self,
        screen,
        player,
        x,
        y,
        width,
        height,
        speed,
        hitbox,
        idle_animation,
        walk_animation,
        pathfinding_distance,
    ):
        super().__init__(
            screen,
            x,
            y,
            width,
            height,
            hitbox,
            idle_animation,
            walk_animation,
        )
        self.player = player
        
        self.speed = speed

        self.spawn_point = (self.x, self.y)
        self.pathfinding_distance = pathfinding_distance
        
        self.player_targeted = False
        self.alert = Alert(screen, self.x + self.width / 2 - 24, self.y + 20)

        self.direction_x = 0
        self.direction_y = 0
        self.distance = 0

    def return_to_spawn(self):
        self.direction_x = self.spawn_point[0] - self.x
        self.direction_y = self.spawn_point[1] - self.y
        self.distance = math.hypot(self.direction_x, self.direction_y)

        if self.distance < 1:
            self.distance = 0
            self.x, self.y = self.spawn_point
            self.flip = False

    def pathfind(self):
        direction_x = self.player.x - self.x
        direction_y = self.player.y - self.y
        distance_squared = direction_x**2 + direction_y**2

        if distance_squared < (self.pathfinding_distance * 10) ** 2:
            self.player_targeted = True
            self.direction_x = direction_x
            self.direction_y = direction_y
            self.distance = math.sqrt(distance_squared)
        else:
            self.player_targeted = False
            self.return_to_spawn()
    
    def draw(self, debug):
        super().draw(debug)
        
        if self.player_targeted:
            self.alert.draw()

    def update(self):
        super().update()

        self.pathfind()

        if self.distance == 0:
            self.moving = False
            return
        
        if self.player_targeted:
            self.alert.x = self.x + self.width / 2 - 24
            self.alert.y = self.y + 20
            self.alert.update()

        direction_x = self.direction_x / self.distance
        direction_y = self.direction_y / self.distance

        self.x += direction_x * self.speed
        self.y += direction_y * self.speed

        self.flip = direction_x < 0
        self.moving = True
