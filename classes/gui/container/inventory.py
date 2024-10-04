from classes.gui.container.container import Container


class Inventory(Container):
    def __init__(self, screen, savedata):
        super().__init__(screen, "Inventory", (4, 4), gap=8)
        self.savedata = savedata
