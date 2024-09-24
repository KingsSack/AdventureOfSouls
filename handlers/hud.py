

class HUD:
    def __init__(self, screen, savedata):
        self.screen = screen
        self.unlocked_buttons = savedata.data.get("unlocked_buttons", [])
    
    def draw(self):
        for button in self.unlocked_buttons:
            button.draw()
    
    def update(self):
        for button in self.unlocked_buttons:
            button.update()
