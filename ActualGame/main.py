import time, os, sys
from os import system, name

# Renaming of the ones used most often
from time import sleep as s
import random as r

#Clears all variables on start (defines them)
#this is for loading and input cmds
userinp = 0
randamt = 0

#This is all of your armor, exp, level, dmg, hp, etc
name = 0
xp = 0
maxxp = 0
level = 0
dmg = 0
hp = 0
maxhp = 0
usedheal = 0
dfn = 0
maxdfn = 0
luck = 0
mp = 0
maxmp = 0
stp = 0
useddfn = 0
usedmp = 0
useddmg = 0
usedluck = 0

#Your inventory and equips
helm = 0
chest = 0
legs = 0
wpn = 0
helmdfn = 0
chestdfn = 0
legsdnf = 0
wpndmg = 0

#enemy stuff
enhp = 0
enmaxhp = 0
endfn = 0
enmaxdfn = 0
endmg = 0
enmp = 0
enmaxmp = 0

# All of the defines
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def logo():
    clear()
    print("\n\n")
    print("[notloaded]")
    print("[notloaded]")
    print("[notloaded]")
    print("[notloaded]")
    print("[notloaded]")
    print("[notloaded]")
    print("[notloaded]")
    print("[notloaded]")
    print("[notloaded]")
    print("\n\n")

def lsn():
    logo()
    userinp = int(input("Have you played before (Do you have save data) Yes (1) or No (2): "))
    if userinp == 1:
        print("Loging in...")
        s(2)
        loading()
        login()
    elif userinp == 2:
        print("Lets get you signed up!")
        s(2)
        loading()
        signup()
    else:
        print("That is not a valid option, the Valid options are 1 and 2, plase try again.")
        s(2)
        lsn()

def hub():
    logo()
    userinp = int(input("Welcome to textbasedrpg! please type '1' to open the command list! (or type 99 to close the game.): "))

    #all of the if's
    if userinp == 1:
        selectionmenu()
    elif userinp == 99:
        print("Cya")
        s(1)
        clear()
        sys.exit()
    else:
        print("Invalid selection")
        s(1)
        hub()
    
def login():
    global name, xp, maxxp, stp, level, dmg, hp, maxhp, usedheal, dfn, maxdfn, luck, mp, maxmp, helm, chest, legs, wpn, helmdfn, chestdfn, legsdnf, wpndmg, useddfn, usedmp, useddmg, usedluck
    with open('svc.xyz', 'r') as file:
        name, xp, maxxp, stp, level, dmg, hp, maxhp, usedheal, dfn, maxdfn, luck, mp, maxmp, helm, chest, legs, wpn, helmdfn, chestdfn, legsdnf, wpndmg, useddfn, usedmp, useddmg, usedluck = file.read().split(',')
        name = str(name)
        xp = int(xp)
        maxxp = int(maxxp)
        stp = int(stp)
        level = int(level)
        dmg = int(dmg)
        hp = int(hp)
        maxhp = int(maxhp)
        usedheal = int(usedheal)
        dfn = int(dfn)
        maxdfn = int(maxdfn)
        luck = int(luck)
        mp = int(mp)
        maxmp = int(maxmp)
        helm = str(helm)
        chest = str(chest)
        legs = str(legs)
        wpn = str(wpn)
        helmdfn = int(helmdfn)
        chestdfn = int(chestdfn)
        legsdnf = int(legsdnf)
        wpndmg = int(wpndmg)
        useddfn = int(useddfn)
        usedmp = int(usedmp)
        useddmg = int(useddmg)
        usedluck = int(usedluck)
        s(.1)
        print(name)
        s(.5)
    hub()

def signup():
    global name, xp, maxxp, stp, level, dmg, hp, maxhp, dfn, maxdfn, luck, mp, maxmp, helm, chest, legs, wpn, helmdfn, chestdfn, legsdnf, wpndmg, useddfn, usedmp, useddmg, usedluck
    name = input("Enter your character name: ")
    xp = 0
    maxxp = 10
    stp = 69
    level = 1
    dmg = 5
    hp = 20
    maxhp = 20
    dfn = 0
    maxdfn = 0
    luck = 0
    mp = 10
    maxmp = 10
    helm = 0
    chest = 0
    legs = 0
    wpn = 0
    helmdfn = 0
    chestdfn = 0
    legsdnf = 0
    wpndmg = 0
    usedheal = 0
    useddfn = 0
    usedmp = 0
    useddmg = 0
    usedluck = 0
    save()
    hub()

def save():
    with open('svc.xyz', 'w') as file:
        file.write(f"{name},{xp},{maxxp},{stp},{level},{dmg},{hp},{maxhp},{usedheal},{dfn},{maxdfn},{luck},{mp},{maxmp},{helm},{chest},{legs},{wpn},{helmdfn},{chestdfn},{legsdnf},{wpndmg},{useddfn},{usedmp},{useddmg},{usedluck}")

def loading():
    randamt = 0
    randamt = r.randint(1, 3)
    while randamt > 0:
        logo()
        print("Loading")
        s(.2)
        logo()
        print("Loading.")
        logo()
        print("Loading..")
        s(.2)
        logo()
        print("Loading...")
        s(.2)
        randamt = randamt - 1

def selectionmenu():
    logo()
    print(f"-------------\nSelection Menu\n---------------\n1. Closes the selection menu\n2. Opens the game\n3. Opens the Stats Menu\n4. Saves You're Game.\n5. [doesnt exist]")
    userinp = int(input("Selection Menu: "))

    #ifs
    if userinp == 1:
        hub()
    elif userinp == 2:
        game()
    elif userinp == 3:
        stats()
    elif userinp == 4:
        save()
        print("Game Saved")
        s(2)
        selectionmenu()
    else:
        print("That does not exist, Sorry.")
        s(2)
        selectionmenu()

def game():
    pass

def stats():
    logo()
    print(f"-------------------\nStats\n-------------------\nName: {name}\nLevel: {level} ({xp}/{maxxp})\nHealth {hp}/{maxhp}\nDefence: {dfn}/{maxdfn}\nMana: {mp}/{maxmp}\nDamage: {dmg}\nLuck: {luck}\n-------------------\nUnused Stat Points: {stp}\n-------------------\n")
    userinp = int(input("Use Your statpoints (1) or Leave the Menu (2): "))
    if userinp == 1:
        stlvl()
    else:
        hub()

def stlvl():
    global stp, maxhp, maxdfn, maxmp, dmg, luck, usedheal, useddfn, usedmp, useddmg, usedluck
    save()
    logo()
    print(f"-------------------\nLevel Up Your Stats\n-------------------\n1. HP {maxhp}\n2. Defence {maxdfn}\n3. Mana {maxmp}\n4. Damage {dmg}\n5. Luck {luck}\n-------------------\nRemaining Statpoints: {stp}\n-------------------")
    userinp = int(input("Type a Number (1-5) to increase a stat or type (99) to exit: "))

    if userinp == 1:
        stp = stp - 1
        usedheal = usedheal + 1
        maxhp = int(maxhp + (1 * (usedheal/2)))
        stlvl()

    elif userinp == 2:
        stp = stp - 1
        useddfn = useddfn + 1
        maxdfn = int(maxdfn + (1 * (useddfn/2)))
        stlvl()

    elif userinp == 3:
        stp = stp - 1
        usedmp = usedmp + 1
        maxmp = int(maxmp + (1 * (usedmp/2)))
        stlvl()

    elif userinp == 4:
        stp = stp - 1
        useddmg = useddmg + 1
        dmg = int(dmg + (1 * (useddmg/2)))
        stlvl()

    elif userinp == 5:
        stp = stp - 1
        usedluck = usedluck + 1
        luck = int(luck + (1 * (usedluck/2)))
        stlvl()

    elif userinp == 99:
        stats()
    
    elif not userinp.lstrip('-').isdigit():
        save()
        print("You almost lost your save.")
        s(2)
        print("to prevent the almost loss of your save type a number next time.")
        s(1)
        print("I saved your stuff so once this dissaperes, you're good, if you close it before then, your save file is cooked")
        s(3)
        print("properly saved")
        s(.2)
        stlvl()

    else:
        print("That isnt a valid Input")
        save()
        s(2)
        stlvl()

lsn()
