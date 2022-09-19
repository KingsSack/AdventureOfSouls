import savedata

def console_commands():
    if input() == "!spell thunder":
        if savedata.thunder_spell != 1:
            savedata.thunder_spell = 1
            if savedata.spell_slot1 == "empty":
                savedata.spell_slot1 = "thunder"
            else:
                if savedata.spell_slot1 != "thunder" and savedata.spell_slot3 != "thunder" and savedata.spell_slot2 == "empty":
                    savedata.spell_slot2 = "thunder"
                else:
                    if savedata.spell_slot2 != "thunder" and savedata.spell_slot1 != "thunder" and savedata.spell_slot3 == "empty":
                        savedata.spell_slot3 = "thunder"
    
    if input() == "!spell thunder":
        if savedata.fireball_spell != 1:
            savedata.fireball_spell = 1
            if savedata.spell_slot1 == "empty":
                savedata.spell_slot1 = "fireball"
            else:
                if savedata.spell_slot1 != "fireball" and savedata.spell_slot3 != "fireball" and savedata.spell_slot2 == "empty":
                    savedata.spell_slot2 = "fireball"
                else:
                    if savedata.spell_slot2 != "fireball" and savedata.spell_slot1 != "fireball" and savedata.spell_slot3 == "empty":
                        savedata.spell_slot3 = "fireball"
    # if input() == "!speed":
    #     new_speed1 = input("Enter new speed1: ")
    #     savedata.speed1 = new_speed1
    #     new_speed2 = input("Enter new speed2: ")
    #     savedata.speed2 = new_speed2
        