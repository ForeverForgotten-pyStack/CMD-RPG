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
stp = 0
useddfn = 0
usedmp = 0
useddmg = 0

#enemy stuff
enhp = 0
enmaxhp = 0
endmg = 0

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
    print("  ______   __       __  _______         _______   _______    ______  ")
    print(" /      \ |  \     /  \|       \       |       \ |       \  /      \ ")
    print("|  $$$$$$\| $$\   /  $$| $$$$$$$\      | $$$$$$$\| $$$$$$$\|  $$$$$$\")
    print("| $$   \$$| $$$\ /  $$$| $$  | $$      | $$__| $$| $$__/ $$| $$ __\$$")
    print("| $$      | $$$$\  $$$$| $$  | $$      | $$    $$| $$    $$| $$|    \")
    print("| $$   __ | $$\$$ $$ $$| $$  | $$      | $$$$$$$\| $$$$$$$ | $$ \$$$$")
    print("| $$__/  \| $$ \$$$| $$| $$__/ $$      | $$  | $$| $$      | $$__| $$")
    print(" \$$    $$| $$  \$ | $$| $$    $$      | $$  | $$| $$       \$$    $$")
    print("  \$$$$$$  \$$      \$$ \$$$$$$$        \$$   \$$ \$$        \$$$$$$ ")
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
    userinp = int(input("Welcome to CMD RPG! please type '1' to open the command list! (or type 99 to close the game.): "))

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
    global name, xp, maxxp, stp, level, dmg, hp, maxhp, usedheal, dfn, maxdfn, luck, mp, maxmp, useddfn, usedmp, useddmg
    with open('svc.xyz', 'r') as file:
        name, xp, maxxp, stp, level, dmg, hp, maxhp, usedheal, dfn, maxdfn, useddfn, useddmg = file.read().split(',')
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
        useddfn = int(useddfn)
        usedmp = int(usedmp)
        useddmg = int(useddmg)
        s(.1)
        print(name)
        s(.5)
    hub()

def signup():
    global name, xp, maxxp, stp, level, dmg, hp, maxhp, dfn, maxdfn, useddfn, useddmg
    name = input("Enter your character name: ")
    xp = 0
    maxxp = 10
    stp = 5
    level = 1
    dmg = 5
    hp = 20
    maxhp = 20
    dfn = 0
    maxdfn = 0
    usedheal = 0
    useddfn = 0
    usedmp = 0
    useddmg = 0
    save()
    hub()

def save():
    with open('svc.xyz', 'w') as file:
        file.write(f"{name},{xp},{maxxp},{stp},{level},{dmg},{hp},{maxhp},{usedheal},{dfn},{maxdfn},{useddfn},{useddmg}")

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
    print(f"-------------\nSelection Menu\n---------------\n1. Closes the selection menu\n2. Opens the game\n3. Opens the Stats Menu\n4. Saves Your Game.\n5. [doesnt exist]")
    userinp = int(input("Selection Menu: "))

    #ifs
    if userinp == 1:
        loading()
        hub()
    elif userinp == 2:
        loading()
        gamelist()
    elif userinp == 3:
        loading()
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
    
def stats():
    logo()
    print(f"-------------------\nStats\n-------------------\nName: {name}\nLevel: {level} ({xp}/{maxxp})\nHealth {hp}/{maxhp}\nDefence: {dfn}/{maxdfn}\nDamage: {dmg}\n-------------------\nUnused Stat Points: {stp}\n-------------------\n")
    userinp = input("Use Your statpoints (1) or Leave the Menu (2): ")
    if userinp == "1":
        stlvl()
    else:
        hub()

def stlvl():
    global stp, maxhp, maxdfn, dmg, usedheal, useddfn, usedmp, useddmg
    save()
    logo()
    print(f"-------------------\nLevel Up Your Stats\n-------------------\n1. HP {maxhp}\n2. Defence {maxdfn}\n3. Damage {dmg}\n-------------------\nRemaining Statpoints: {stp}\n-------------------")
    
    if stp > 0:
        userinp = input("Type a Number (1-5) to increase a stat or type (99) to exit: ")

        if userinp == "1":
            stp = stp - 1
            usedheal = usedheal + 1
            maxhp = int(maxhp + (1 * (usedheal/2)))
            stlvl()

        elif userinp == "2":
            stp = stp - 1
            useddfn = useddfn + 1
            maxdfn = int(maxdfn + (1 * (useddfn/2)))
            stlvl()


        elif userinp == "3":
            stp = stp - 1
            useddmg = useddmg + 1
            dmg = int(dmg + (1 * (useddmg/2)))
            stlvl()

        elif userinp == "99":
            stats()
        
        else:
            print("That isnt a valid Input")
            save()
            s(2)
            stlvl()
    else:
        print("You dont have any statpoints to use.")
        print("type anything to contenue")
        userinp = input("")
        stats()



#This is where the actual game will be located, all the fighting stuff will be here


        
def gamelist():
    logo()
    print(f"------------------------------\nLocations/Actions to Begin (type the number)\n------------------------------\n1. Dive In\n2. Stats\n3. Quit Back To Menu")
    userinp = input("------------------------------\nAction Menu: ")

    if userinp == "1":
        dive()
    
    if userinp == "2":
        gamestats()
    
    if userinp == "3":
        hub()
    else:
        print("That isnt a working command. trying again...")
        s(1)
        gamelist()

def gamestats():
    logo()
    print(f"-------------------\nStats\n-------------------\nName: {name}\nLevel: {level} ({xp}/{maxxp})\nHealth {hp}/{maxhp}\nDefence: {dfn}/{maxdfn}\nDamage: {dmg}\n-------------------\nUnused Stat Points: {stp}\n-------------------\n")
    userinp = input("Once your ready type anything to exit: ")
    gamelist()

def dive():
    logo()
    print("Now before you begin, the fights are INSTANT, you cannot heal or anything like that. DEATH WILL WIPE YOUR SAVE")
    s(2)
    war()

def war():
    global endmg, enhp, el, xp, maxxp, stp, maxhp, maxdfn, dmg, dfn, hp, dmg, usedheal, useddfn, useddmg, level, gxp

    logo()
    
    print("Now what level do you want the enemy to be?")
    el = int(input("------------------------------\nAction Menu: "))
    print("Now lets see how long you can last. Good luck.")
    s(1)
    clear()
    logo()

    # Initialize enemy stats
    eh = 0
    hdmg = 0
    ph = 0
    gxp = 0

    # Calculate enemy stats based on level
    endmg = endmg + (2 + int(el/.5))
    enhp = enhp + (5 + int(el/.5))

    def runz():
        global endmg, enhp, el, xp, maxxp, stp, maxhp, maxdfn, dmg, dfn, hp, dmg, usedheal, useddfn, useddmg, level, gxp

        if enhp > 0 and hp > 0:
            # Enemy attack
            eh = r.randint(1, endmg) - dfn
            dfn = dfn - eh
            hp = hp - eh

            # Player attack
            hdmg = int(dmg * .5)
            ph = r.randint(hdmg, dmg)
            gxp = gxp + 1 + int(ph/5)
            enhp = enhp - ph

        # Victory condition
        if enhp <= 0 and hp > 0:
            print(f"You won with {hp}/{maxhp} remaining and gained {gxp} XP!")
            hp = maxhp
            dfn = maxdfn
            xp = xp + gxp
            
            # Level up check
            if xp >= maxxp:
                xp = xp - maxxp
                maxxp = int(maxxp * 1.25)
                level = level + 1
                stp = stp + 1
                print(f"Level up! You now have {stp} Status Points for use!")
            
            s(2)
            save()
            gamelist()

        # Defeat condition
        if hp <= 0:
            savewipe()

    # Main combat loop
    while enhp > 0 and hp > 0:
        runz()

        

def savewipe():
    global endmg, enhp, el, xp, maxxp, stp, maxhp, maxdfn, dmg, dfn, hp, dmg, usedheal, useddfn, useddmg, level, gxp
    print("You died... wiping your save, sorry.")
    xp = 0
    maxxp = 10
    stp = 5
    level = 1
    dmg = 5
    hp = 20
    maxhp = 20
    dfn = 0
    maxdfn = 0
    usedheal = 0
    useddfn = 0
    usedmp = 0
    useddmg = 0
    save()
    s(1)
    hub()






lsn()
