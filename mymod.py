import sys
from os import system


def chktypes(tayp):
    Types = ("Normal", "Fire", "Fighting", "Water", "Flying", "Grass", "Poison", "Electric", "Ground", "Psychic",
             "Rock", "Ice", "Bug", "Dragon", "Ghost", "Dark", "Steel", "Fairy", "???")

    tflag = 0
    for i in range(19):
        if tayp == Types[i]:
            tflag = 1

    if tflag == 0:
        print("Please select only on the list, restart program")
        sys.exit()

def chkweather(weder):
    Weathers = ("Normal", "Sunny", "Rain", "Sandstorm", "Hail", "Other")

    wflag = 0
    for i in range(6):
        if weder == Weathers[i]:
            wflag = 1

    if wflag == 0:
        print("Please select only on the list, restart program")
        sys.exit()

def dmgtbst(dmg):
    system("cls")
    print("Data for Damage")
    print("Level:   ", dmg[0])
    print("Attack:  ", dmg[1])
    print("Power:   ", dmg[2])
    print("Defense: ", dmg[3])
    print("Modifier:", dmg[4])

def modtbst(mod):
    if mod[2] == 2:
        print("Data for Modifier")
        print("Target:          ", mod[0])
        print("Weather:         ", mod[1])
        print("Generation:      ", mod[2])
        print("Badge:           ", mod[3])
        print("Critical:        ", mod[4])
        print("Random:          ", mod[5])
        print("STAB:            ", mod[6])
        print("Effectiveness:   ", mod[7])
        print("Burn:            ", mod[8])
        print("other:           ", mod[9])
    else:
        print("Data for Modifier")
        print("Target:          ", mod[0])
        print("Weather:         ", mod[1])
        print("Critical:        ", mod[4])
        print("Random:          ", mod[5])
        print("STAB:            ", mod[6])
        print("Effectiveness:   ", mod[7])
        print("Burn:            ", mod[8])
        print("other:           ", mod[9])