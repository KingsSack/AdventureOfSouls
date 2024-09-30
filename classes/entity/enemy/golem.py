from classes.collider import Collider
from classes.entity.enemy.enemy import Enemy


class Golem(Enemy):
    def __init__(self, screen, player, x, y):
        super().__init__(
            screen,
            player,
            x=x,
            y=y,
            width=225,
            height=160,
            speed=1,
            hitbox=Collider(self, 75, 80, 75, 80),
            idle_animation="golem_idle",
            walk_animation="golem_walk",
            pathfinding_distance=40,
        )
