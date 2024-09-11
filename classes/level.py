from dataclasses import dataclass


@dataclass
class Level:
    name: str
    background_color: tuple
    surrounding_levels: dict
    layer_1: list
    layer_2: list
    objects: dict
    entities: dict
    enemies: dict
    npcs: dict
