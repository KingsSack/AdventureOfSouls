import savedata
import game

def console_commands():
    if input() == "!spell thunder":
        game.main_character.wizardThunder()
    # if input() == "!speed":
    #     new_speed1 = input("Enter new speed1: ")
    #     savedata.speed1 = new_speed1
    #     new_speed2 = input("Enter new speed2: ")
    #     savedata.speed2 = new_speed2
        