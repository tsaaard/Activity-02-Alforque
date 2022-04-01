import sys
from time import sleep
from os import system


def chktypes(tayp):
    Types = ("Normal", "Fire", "Fighting", "Water", "Flying", "Grass", "Poison", "Electric", "Ground", "Psychic",
             "Rock", "Ice", "Bug", "Dragon", "Ghost", "Dark", "Steel")

    tflag = 0
    for i in range(17):
        if tayp == Types[i]:
            tflag = 1

    if tflag == 0:
        print("Please select only on the list, restart program")
        sleep(3)
        sys.exit()
        
def chkweather(weder):
    Weathers = ("Normal", "Sunny", "Rain", "Sandstorm", "Hail", "Other")

    wflag = 0
    for i in range(6):
        if weder == Weathers[i]:
            wflag = 1

    if wflag == 0:
        print("Please select only on the list, restart program")
        sleep(3)
        sys.exit()

def dflagz(n1, n2):
    val = 0
    if n1 == 0 or n2 == 0:
        val = 0
    else:
        if n1 == 0.5:
            if n2 == 0.5:
                val = 0.25
            elif n2 == 1:
                val = 0.5
            elif n2 == 2:
                val = 1
        elif n2 == 0.5:
            if n1 == 0.5:
                val = 0.25
            elif n1 == 1:
                val = 0.5
            elif n1 == 2:
                val = 1
        elif n1 == 1:
            if n2 == 0.5:
                val = 0.5
            elif n2 == 1:
                val = 1
            elif n2 == 2:
                val == 2
        elif n2 == 1:
            if n1 == 0.5:
                val = 0.5
            elif n1 == 1:
                val = 1
            elif n1 == 2:
                val == 2
        elif n1 == 2:
            if n2 == 0.5:
                val = 1
            elif n2 == 1:
                val = 2
            elif n2 == 2:
                val = 4
        elif n2 == 2:
            if n1 == 0.5:
                val = 1
            elif n1 == 1:
                val = 2
            elif n1 == 2:
                val = 4   
    return val


def dmgtbst(dmg):
    system("cls")
    print("Data for Damage")
    print("Level:   ", dmg[0])
    print("Attack:  ", dmg[1])
    print("Power:   ", dmg[2])
    print("Defense: ", dmg[3])
    print("Modifier:", dmg[4])

def modtbst(mod):
    print("Data for Modifier")
    print("Target:          ", mod[0])
    print("Weather:         ", mod[1])
    print("Critical:        ", mod[2])
    print("Random:          ", mod[3])
    print("STAB:            ", mod[4])
    print("Effectiveness:   ", mod[5])
    print("Burn:            ", mod[6])
    print("other:           ", mod[7])
    sleep(5)