

class HUD:
    def __init__(self, screen, savedata):
        self.screen = screen
        self.savedata = savedata
        
        self.unlocked_menu_buttons = self.savedata.get_or_set_default("unlocked_buttons", [])
    
    def draw(self):
        for button in self.unlocked_menu_buttons:
            button.draw()
    
    def update(self):
        for button in self.unlocked_menu_buttons:
            button.update()
