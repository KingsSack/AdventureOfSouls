

from classes.entity import Entity


class NPC(Entity):
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
        dialogue: str,
        interaction : bool = False,
    ):
        super().__init__(
            screen,
            x,
            y,
            width,
            height,
            speed,
            hitbox,
            idle_animation,
            walk_animation,
        )
        self.player = player
        self.dialogue = dialogue
        self.interaction = interaction
        
