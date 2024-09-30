from classes.hud.container.container import Container


class Inventory(Container):
    def __init__(self, screen):
        super().__init__(screen, 400, 400, "inventory", (4, 4))
