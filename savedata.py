
t = 0

tutorial_level = 0

speed1 = 3
speed2 = 5

spell_slot1 = "empty"
spell_slot2 = "empty"
spell_slot3 = "empty"

fireball_spell = 0
thunder_spell = 0
shadow_spell = 0
sprint_spell = 0

inventory = {}
for i in range(36):
    inventory[i + 1] = ""

def load():
    """ later """

def save():
    with open('readme.txt', 'w') as f:
        f.writelines([f'speed1: {speed1}', f'speed2: {speed2}', "",
                      f'spell1: {spell_slot1}', f'spell2: {spell_slot2}', f'spell3: {spell_slot3}', "",
                      f'fireball: {fireball_spell}', f'thunder: {thunder_spell}', f'shadow: {shadow_spell}', f'sprint: {sprint_spell}', "",
                      f'inventory: {inventory}'])
        
        f.close()
