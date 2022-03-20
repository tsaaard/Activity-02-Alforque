from glob import escape
import sys
import random
from os import system
import mymod  # user defined module

system("cls")

Weathers = ("Normal", "Sunny", "Rain", "Sandstorm", "Hail", "Other")

Badges = ("Zephyr", "Hive", "Plain", "Fog", "Storm", "Mineral", "Glacier", "Rising",
          "Boulder", "Cascade", "Thunder",  "Rainbow", "Soul", "Marsh", "Volcano",)

Level = int(input("Pokemon Level: "))
Attack = int(input("Attack Power: "))
Defense = int(input("Enemy Defense: "))
Power = int(input("Skill Power: "))
Damage = 0

# Type Determining
system("cls")
print("""Types:
- Normal       - Grass        - Rock        - Dark
- Fire         - Poison       - Ice         - Steel
- FIghting     - Electric     - Bug         - Fairy
- Water        - Ground       - Dragon      - ???
- Flying       - Psychic      - Ghost""")
U_Type = input("User Type: ")
mymod.chktypes(U_Type)
A_Type = input("Attack Type: ")
mymod.chktypes(A_Type)
Type_C = input("Is the target a single type? y/n: ")
if Type_C == 'y':
    E_TypeOne = input("Enemy Type: ")
    mymod.chktypes(E_TypeOne)
elif Type_C == 'n':
    system("cls")
    print("Feature not yet ready. Sorry for the inconvenience.")
    sys.exit()
    E_TypeOne = input("Enemy 1st Type: ")
    mymod.chktypes(E_TypeOne)
    E_TypeTwo = input("Enemy 2nd Type: ")
    mymod.chktypes(E_TypeTwo)
else:
    system("cls")
    print("Invalid Input, restart program")
    sys.exit()

# Target
system("cls")
Target = int(input("How many Target: "))
ttvalue = 0.0
if Target == 1:
    ttvalue = 1
elif Target == 2:
    ttvalue = 0.5
else:
    print("One or Two only, restart program")

# Weather
system("cls")
wrvalue = 0.0
print("""Weathers:
 - Normal    - Sandstorm
 - Sunny    - Hail
 - Rain     - Other""")
Weather = input("Select Weather: ")
mymod.chkweather(Weather)
if Weather == Weathers[1] and A_Type == "Fire":
    wrvalue = 1.5
elif Weather == Weathers[1] and A_Type == "Water":
    wrvalue = 0.5
elif Weather == Weathers[2] and A_Type == "Water":
    wrvalue = 1.5
elif Weather == Weathers[2] and A_Type == "Fire":
    wrvalue = 0.5
else:
    wrvalue = 1

# Badge
system("cls")
Generation = int(input("Generation: "))
bflag = 0
bevalue = 0.0
if Generation == 2:
    Badge = input("Badge: ")
    for i in range(15):
        if Badge == Badges[i]:
            bflag = 1
    if bflag == 1:
        if Badge == "Zephyr" and A_Type == "Flying":
            bevalue = 1.25
        elif Badge == "Hive" and A_Type == "Bug":
            bevalue = 1.25
        elif Badge == "Plain" and A_Type == "Normal":
            bevalue = 1.25
        elif Badge == "Fog" and A_Type == "Ghost":
            bevalue = 1.25
        elif Badge == "Storm" and A_Type == "Fighting":
            bevalue = 1.25
        elif Badge == "Mineral" and A_Type == "Steel":
            bevalue = 1.25
        elif Badge == "Glacier" and A_Type == "Ice":
            bevalue = 1.25
        elif Badge == "Rising" and A_Type == "Dragon":
            bevalue = 1.25
        elif Badge == "Boulder" and A_Type == "Rock":
            bevalue = 1.25
        elif Badge == "Cascade" and A_Type == "Water":
            bevalue = 1.25
        elif Badge == "Thunder" and A_Type == "Electric":
            bevalue = 1.25
        elif Badge == "Rainbow" and A_Type == "Grass":
            bevalue = 1.25
        elif Badge == "Soul" and A_Type == "Poison":
            bevalue = 1.25
        elif Badge == "Marsh" and A_Type == "Psychic":
            bevalue = 1.25
        elif Badge == "Volcano" and A_Type == "Fire":
            bevalue = 1.25
        else:
            bevalue = 1
    else:
        system("cls")
        print("Badge not found, restart program")
        sys.exit()

# Critical
chance = [1, 2]
Critical = random.choice(chance)
clvalue = 0
if Critical == 1:
    clvalue = 2
else:
    clvalue = 1

# Random
Random = random.uniform(0.85, 1.00)

# STAB
sbvalue = 0
if U_Type == A_Type:
    sbvalue = 1.5
else:
    sbvalue = 1

# Effectiveness
D_Types = ("Normal", "Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire",
             "Water", "Grass", "Electro", "Psychic", "Ice", "Dragon", "Dark", "Fairy", "???")
esvalue = 0.0
if Type_C == 'y':  # Single type enemy
    if A_Type == "Normal":  # Attack Type: Normal
        for i in range(19):
            if E_TypeOne == D_Types[i]:
                if i == 5 or i == 8:
                    esvalue = 0.5
                elif i == 7:
                    esvalue = 0.0
                else:
                    esvalue = 1
    elif A_Type == "Fighting":  # Attack Type: Fighting
        for i in range(19):
            if E_TypeOne == D_Types[i]:
                if i == 2 or i == 3 or i == 6 or i == 13 or i == 17:
                    esvalue = 0.5
                elif i == 0 or i == 5 or i == 8 or i == 14 or i == 16:
                    esvalue = 2.0
                elif i == 7:
                    esvalue = 0.0
                else:
                    esvalue = 1
    elif A_Type == "Flying":  # Attack Type: Flying
        if E_TypeOne == D_Types[i]:
                if i == 5 or i == 8 or i == 12:
                    esvalue = 0.5
                elif i == 1 or i == 6 or i == 11:
                    esvalue = 2.0
                else:
                    esvalue = 1
    elif A_Type == "Poison":  # Attack Type: Poison
        if E_TypeOne == D_Types[i]:
                if i == 3 or i == 4 or i == 5 or i == 7:
                    esvalue = 0.5
                elif i == 11 or i == 17:
                    esvalue = 2.0
                elif i == 8:
                    esvalue = 0.0
                else:
                    esvalue = 1
    elif A_Type == "Ground":  # Attack Type: Ground
        if E_TypeOne == D_Types[i]:
                if i == 6 or i == 11:
                    esvalue = 0.5
                elif i == 3 or i == 5 or i == 8 or i == 9 or i == 12:
                    esvalue = 2.0
                elif i == 2:
                    esvalue = 0.0
                else:
                    esvalue = 1
    elif A_Type == "Rock":  # Attack Type: Rock
        if E_TypeOne == D_Types[i]:
                if i == 1 or i == 4 or i == 8:
                    esvalue = 0.5
                elif i == 2 or i == 6 or i == 9 or i == 14:
                    esvalue = 2.0
                else:
                    esvalue = 1
    elif A_Type == "Bug":  # Attack Type: Bug
        if E_TypeOne == D_Types[i]:
                if i == 1 or i == 2 or i == 3 or i == 7 or i == 8 or i == 9 or i == 17:
                    esvalue = 0.5
                elif i == 11 or i == 13 or i == 16:
                    esvalue = 2.0
                else:
                    esvalue = 1
    elif A_Type == "Ghost":  # Attack Type: Ghost
        for i in range(19):
            if E_TypeOne == D_Types[i]:
                if i == 16:
                    esvalue = 0.5
                elif i == 7 or i == 13:
                    esvalue = 2.0
                elif i == 0:
                    esvalue = 0.0
                else:
                    esvalue = 1
    elif A_Type == "Steel":  # Attack Type: Steel
        for i in range(19):
            if E_TypeOne == D_Types[i]:
                if i == 8 or i == 9 or i == 10 or i == 12:
                    esvalue = 0.5
                elif i == 5 or i == 14 or i == 17:
                    esvalue = 2.0
                else:
                    esvalue = 1
    elif A_Type == "Fire":  # Attack Type: Fire
        for i in range(19):
            if E_TypeOne == D_Types[i]:
                if i == 5 or i == 9 or i == 10 or i == 15:
                    esvalue = 0.5
                elif i == 6 or i == 8 or i == 11 or i == 14:
                    esvalue = 2.0
                else:
                    esvalue = 1
    elif A_Type == "Water":  # Attack Type: Water
        for i in range(19):
            if E_TypeOne == D_Types[i]:
                if i == 10 or i == 11 or i == 15:
                    esvalue = 0.5
                elif i == 4 or i == 5 or i == 9:
                    esvalue = 2.0
                else:
                    esvalue = 1
    elif A_Type == "Grass":  # Attack Type: Grass
        for i in range(19):
            if E_TypeOne == D_Types[i]:
                if i == 2 or i == 3 or i == 6 or i == 8 or i == 9 or i == 11 or i == 15:
                    esvalue = 0.5
                elif i == 4 or i == 5 or i == 10:
                    esvalue = 2.0
                else:
                    esvalue = 1
    elif A_Type == "Electric": # Attack Type: Electric
        for i in range(19):
            if E_TypeOne == D_Types[i]:
                if i == 11 or i == 12 or i == 15:
                    esvalue = 0.5
                elif i == 2 or i == 10:
                    esvalue = 2.0
                elif i == 4:
                    esvalue = 0.0
                else:
                    esvalue = 1
    elif A_Type == "Psychic": # Attack Type: Psychic
        for i in range(19):
            if E_TypeOne == D_Types[i]:
                if i == 8 or i == 13:
                    esvalue = 0.5
                elif i == 1 or i == 3:
                    esvalue = 2.0
                elif i == 16:
                    esvalue = 0.0
                else:
                    esvalue = 1
    elif A_Type == "Ice": # Attack Type: Ice
        for i in range(19):
            if E_TypeOne == D_Types[i]:
                if i == 8 or i == 9 or i == 10 or i == 14:
                    esvalue = 0.5
                elif i == 2 or i == 4 or i == 11 or i == 15:
                    esvalue = 2.0
                else:
                    esvalue = 1
    elif A_Type == "Dragon": # Attack Type: Dragon
        for i in range(19):
            if E_TypeOne == D_Types[i]:
                if i == 8:
                    esvalue = 0.5
                elif i == 15:
                    esvalue = 2.0
                elif i == 17:
                    esvalue = 0.0
                else:
                    esvalue = 1
    elif A_Type == "Dark": # Attack Type: Dark
        for i in range(19):
            if E_TypeOne == D_Types[i]:
                if i == 1 or i == 16 or i == 17:
                    esvalue = 0.5
                elif i == 7 or i == 13:
                    esvalue = 2.0
                else:
                    esvalue = 1
    elif A_Type == "Fairy": # Attack Type: Fairy
        for i in range(19):
            if E_TypeOne == D_Types[i]:
                if i == 3 or i == 8 or i == 9:
                    esvalue = 0.5
                elif i == 1 or i == 15 or i == 16:
                    esvalue = 2.0
                else:
                    esvalue = 1

# Burn
system("cls")
Burn = input("User's pokemon burned? y/n: ")
bnvalue = 0.0
if Burn == 'y':
    bnvalue = 0.5
elif Burn == 'n':
    bnvalue = 1
else:
    system("cls")
    print("Invalid input, restart program")
    sys.exit()

# Other
other = 1

# Computation
if Generation == 2:
    Modifier = (ttvalue * wrvalue * bevalue * clvalue *
                Random * sbvalue * esvalue * bnvalue * other)
else:
    Modifier = (ttvalue * wrvalue * clvalue * Random *
                sbvalue * esvalue * bnvalue * other)

Damage = ((((((2 * Level) / 5) + 2) * (Power * (Attack / Defense))) / 50) + 2) * Modifier

system('cls')
print("User Pokemon Type:       ", U_Type)
print("User Pokemon Attack Type:", A_Type)
if Type_C == 'n':
    print("Enemy Pokemon Type:      ", E_TypeOne)
    print("Enemy Pokemon Type:      ", E_TypeTwo)
else:
    print("Enemy Pokemon Type:      ", E_TypeOne)
if esvalue == 2.0 or esvalue == 4.0:
    if clvalue == 2:
        print("Calculated Damage:", Damage, "Super Effective, Critical Hit")
    else:
        print("Calculated Damage:", Damage, "Super Effective")
elif esvalue == 0.25 or esvalue == 0.5:
    if clvalue == 2:
        print("Calculated Damage:", Damage, "Not Very Effective, Critical Hit")
    else:
        print("Calculated Damage:", Damage, "Not Very Effective")
else:
    print("Calculated Damage:", Damage, "Ineffective")

trobol = input("\n\nSee collected data for damage? y/n: ")
if trobol == 'y' or trobol == 'Y':
    dmg_tuple = (Level, Attack, Defense, Power, Modifier)
    mymod.dmgtbst(dmg_tuple)
    trobol = input("\nSee collected data for modifier? y/n: ")
    if trobol == 'y' or trobol == 'Y':
        mod_tuple = (ttvalue, wrvalue, Generation, bevalue, clvalue, Random, sbvalue, esvalue, bnvalue, other)
        mymod.modtbst(mod_tuple)
    elif trobol == 'n' or trobol == 'N':
        print("Okay Bye Bye")
    else:
        print("nu bayan")
elif trobol == 'n' or trobol == 'N':
    print("Okay Bye Bye")
else:
    print("nu bayan")