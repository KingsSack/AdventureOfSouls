from classes.item import Item
from classes.rarity import Rarity


class Cloak(Item):
    def __init__(
        self,
        screen,
        x,
        y,
        icon,
        rarity: Rarity,
        name,
        power_modifier,
        defense_modifier,
        speed_modifier,
        idle_animation,
        walk_animation,
    ):
        super().__init__(screen, x, y, icon, rarity)
        self.name = name
        self.power_modifier = power_modifier
        self.defense_modifier = defense_modifier
        self.speed_modifier = speed_modifier
        
        self.idle_animation = idle_animation
        self.walk_animation = walk_animation
