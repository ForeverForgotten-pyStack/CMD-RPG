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
dfn = 0
maxdfn = 0
luck = 0
mp = 0
maxmp = 0

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
    userinp = int(input("Have you played before (Do you have save data) Yes (1) or No (2)"))
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

def main():
    pass

def login():
    global name, xp, maxxp, level, dmg, hp, maxhp, dfn, maxdfn, luck, mp, maxmp, helm, chest, legs, wpn, helmdfn, chestdfn, legsdnf, wpndmg
    with open('save.xyz', 'r') as file:
        name, xp, maxxp, level, dmg, hp, maxhp, dfn, maxdfn, luck, mp, maxmp, helm, chest, legs, wpn, helmdfn, chestdfn, legsdnf, wpndmg = file.read().split(',')
        name = str(name)
        xp = int(xp)
        maxxp = int(maxxp)
        level = int(level)
        dmg = int(dmg)
        hp = int(hp)
        maxhp = int(maxhp)
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
    main()

def signup():
    global name, xp, maxxp, level, dmg, hp, maxhp, dfn, maxdfn, luck, mp, maxmp, helm, chest, legs, wpn, helmdfn, chestdfn, legsdnf, wpndmg
    name = input("Enter your character name: ")
    xp = 0
    maxxp = 10
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
    save()
    main()

def save():
    with open('save.xyz', 'w') as file:
        file.write(f"{name},{xp},{maxxp},{level},{dmg},{hp},{maxhp},{dfn},{maxdfn},{luck},{mp},{maxmp},{helm},{chest},{legs},{wpn},{helmdfn},{chestdfn},{legsdnf},{wpndmg}")

def loading():
    if randamt != 0:
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

lsn()
