import savedata

class ConsoleCommands():
    def __init__(self):
        super().__init__()
    
    def spell(self, spell_name):
        if savedata.spell_slot1 == "empty":
            savedata.spell_slot1 = spell_name
        else:
            if savedata.spell_slot1 != spell_name and savedata.spell_slot3 != spell_name and savedata.spell_slot2 == "empty":
                savedata.spell_slot2 = spell_name
            else:
                if savedata.spell_slot2 != spell_name and savedata.spell_slot1 != spell_name and savedata.spell_slot3 == "empty":
                    savedata.spell_slot3 = spell_name
    
    def tick(self):
        if input() == "!spell thunder":
            if savedata.thunder_spell != 1:
                savedata.thunder_spell = 1
                self.spell("thunder")
        
        if input() == "!spell fireball":
            if savedata.fireball_spell != 1:
                savedata.fireball_spell = 1
                self.spell("fireball")

        # if input() == "!speed":
        #     new_speed1 = input("Enter new speed1: ")
        #     savedata.speed1 = new_speed1
        #     new_speed2 = input("Enter new speed2: ")
        #     savedata.speed2 = new_speed2
commands = ConsoleCommands()
        