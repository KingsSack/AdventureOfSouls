

from classes.alert import Alert
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
        
        self.alert = Alert(screen, self.x + self.width / 2 - 24, self.y + 20)
    
    def draw(self, debug):
        super().draw(debug)
        
        if self.interaction:
            self.alert.draw()
    
    def update(self):
        super().update()
        
        if self.interaction:
            self.alert.update()
