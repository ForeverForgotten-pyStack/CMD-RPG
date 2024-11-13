from os import system, name
from time import sleep as s
import random as r
import os, sys

userinp = 0
randamt = 0
em = 0

name = xp = maxxp = level = dmg = hp = maxhp = usedheal = dfn = maxdfn = stp = useddfn = usedmp = useddmg = 0
enhp = enmaxhp = endmg = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo():
    clear()
    print("\n\n")
    print("  ______   __       __  _______         _______   _______    ______  ")
    print(" /      \ |  \     /  \|       \       |       \ |       \  /      \ ")
    print("|  $$$$$$\| $$\   /  $$| $$$$$$$\      | $$$$$$$\| $$$$$$$\|  $$$$$$\\")
    print("| $$   \$$| $$$\ /  $$$| $$  | $$      | $$__| $$| $$__/ $$| $$ __\$$")
    print("| $$      | $$$$\  $$$$| $$  | $$      | $$    $$| $$    $$| $$|    \\")
    print("| $$   __ | $$\$$ $$ $$| $$  | $$      | $$$$$$$\| $$$$$$$ | $$ \$$$$")
    print("| $$__/  \| $$ \$$$| $$| $$__/ $$      | $$  | $$| $$      | $$__| $$")
    print(" \$$    $$| $$  \$ | $$| $$    $$      | $$  | $$| $$       \$$    $$")
    print("  \$$$$$$  \$$      \$$ \$$$$$$$        \$$   \$$ \$$        \$$$$$$ ")
    print("\n\n")

def lsn():
    logo()
    userinp = input("Have you played before (Do you have save data) Yes (1) or No (2): ")
    if userinp == "1":
        print("Logging in...")
        s(2)
        loading()
        login()
    elif userinp == "2":
        print("Lets get you signed up!")
        s(2)
        loading()
        signup()
    else:
        print("Valid options are 1 and 2, please try again.")
        s(2)
        lsn()

def login():
    global name, xp, maxxp, stp, level, dmg, hp, maxhp, usedheal, dfn, maxdfn, useddfn, usedmp, useddmg
    with open('svc.xyz', 'r') as file:
        name, xp, maxxp, stp, level, dmg, hp, maxhp, usedheal, dfn, maxdfn, useddfn, useddmg = file.read().split(',')
        name = str(name)
        xp, maxxp, stp, level, dmg, hp, maxhp, usedheal, dfn, maxdfn, useddfn, usedmp, useddmg = map(int, [xp, maxxp, stp, level, dmg, hp, maxhp, usedheal, dfn, maxdfn, useddfn, usedmp, useddmg])
    hub()

def hub():
    logo()
    userinp = input("Welcome to CMD RPG! please type '1' to open the command list! (or type 99 to close the game.): ")
    if userinp == "1": selectionmenu()
    elif userinp == "99":
        print("Cya")
        s(1)
        clear()
        sys.exit()
    else: hub()

def signup():
    global name, xp, maxxp, stp, level, dmg, hp, maxhp, dfn, maxdfn, useddfn, useddmg
    name = input("Enter your character name: ")
    xp = 0
    maxxp = 10
    stp = level = 5
    dmg = 5
    hp = maxhp = 20
    dfn = maxdfn = usedheal = useddfn = usedmp = useddmg = 0
    save()
    hub()

def save():
    with open('svc.xyz', 'w') as file:
        file.write(f"{name},{xp},{maxxp},{stp},{level},{dmg},{hp},{maxhp},{usedheal},{dfn},{maxdfn},{useddfn},{useddmg}")

def loading():
    for _ in range(r.randint(1, 3)):
        for dots in range(4):
            logo()
            print("Loading" + "."*dots)
            s(.2)

def selectionmenu():
    logo()
    print("-------------\nSelection Menu\n---------------\n1. Close Menu\n2. Open Game\n3. Stats Menu\n4. Save Game")
    userinp = input("Selection Menu: ")
    if userinp == "1": hub()
    elif userinp == "2": gamelist()
    elif userinp == "3": stats()
    elif userinp == "4":
        save()
        print("Game Saved")
        s(2)
        selectionmenu()
    else: selectionmenu()

def gamelist():
    logo()
    print("------------------------------\nLocations/Actions\n------------------------------")
    print("1. Dive In\n2. Stats\n3. Back To Menu")
    userinp = input("Action Menu: ")
    
    if userinp == "1": dive()
    elif userinp == "2": gamestats()
    elif userinp == "3": hub()
    else: gamelist()

def dive():
    logo()
    print("Fights are INSTANT - no healing mid-fight. DEATH WILL WIPE YOUR SAVE")
    s(2)
    war()

def gamestats():
    logo()
    print(f"Stats\n-------------------\nName: {name}\nLevel: {level} ({xp}/{maxxp})")
    print(f"Health {hp}/{maxhp}\nDefence: {dfn}/{maxdfn}\nDamage: {dmg}")
    input("Press Enter to return")
    gamelist()

def stats():
    logo()
    print(f"-------------------\nStats\n-------------------\nName: {name}\nLevel: {level} ({xp}/{maxxp})\nHealth {hp}/{maxhp}\nDefence: {dfn}/{maxdfn}\nDamage: {dmg}\n-------------------\nUnused Stat Points: {stp}\n-------------------\n")
    if input("Use statpoints (1) or Leave (2): ") == "1": stlvl()
    else: hub()

def stlvl():
    # Global variables for stat management
    global stp, maxhp, maxdfn, dmg, usedheal, useddfn, usedmp, useddmg
    save()  # Save current state
    
    while True:  # Main stat allocation loop
        logo()
        # Display current stats and menu
        print(f"-------------------\nLevel Up Your Stats\n-------------------")
        print(f"1. HP {maxhp}\n2. Defence {maxdfn}\n3. Damage {dmg}")
        print(f"-------------------\nRemaining Statpoints: {stp}\n-------------------")
        print("\nPress Enter to return to stats menu")
        
        if stp > 0:  # Check for available points
            statsel = input("Select stat (1-3): ")
            
            # Exit condition
            if statsel == "":
                stats()
                return
                
            # Stat allocation section
            if statsel in ["1", "2", "3"]:
                statamt = int(input("How many points to use: "))
                
                if statamt <= stp:
                    while statamt > 0:
                        # HP scaling - uses both investment count and current value
                        if statsel == "1":
                            stp -= 1
                            usedheal += 1
                            maxhp = int(maxhp + (2 * usedheal * 0.25) + (maxhp * 0.1))
                            statamt -= 1
                            
                        # Defense scaling - balanced for steady growth
                        elif statsel == "2":
                            stp -= 1
                            useddfn += 1
                            maxdfn = int(maxdfn + (1 * useddfn * 0.15) + (maxdfn * 0.08))
                            statamt -= 1
                            
                        # Damage scaling - aggressive growth for offensive focus
                        elif statsel == "3":
                            stp -= 1
                            useddmg += 1
                            dmg = int(dmg + (1 * useddmg * 0.2) + (dmg * 0.12))
                            statamt -= 1
                    
                    save()  # Save after spending points
                else:
                    print("Not enough stat points!")
                    s(2)
        else:
            input("\nNo stat points available. Press Enter to return")
            stats()
            return

def war():
    global endmg, enhp, el, xp, maxxp, stp, maxhp, maxdfn, dmg, dfn, hp, dmg, usedheal, useddfn, useddmg, level, gxp, em
    gxp = 0
    logo()
    
    el = int(input("Enemy level: "))
    total_matches = int(input("Number of matches: "))
    matches_remaining = total_matches
    
    while matches_remaining > 0:
        endmg = 2 + int(el/.5)
        enhp = enmaxhp = 5 + int(el/.5)
        round_num = 1
        round_xp = 0
        
        logo()
        print(f"\nMatch {total_matches - matches_remaining + 1} of {total_matches} starting!")
        print(f"Enemy Stats - Max HP: {enmaxhp} | Damage Range: {int(endmg/2)}-{endmg}")
        s(1)

        while True:
            logo()
            print(f"Match {total_matches - matches_remaining + 1}/{total_matches} - Round {round_num}")
            print("-" * 30)
            s(0.5)
            
            # Player attack
            logo()
            hdmg = int(dmg * .5)
            ph = r.randint(hdmg, dmg)
            round_xp = int((ph/3)/enhp + (el/2))
            gxp += round_xp
            enhp -= ph
            print(f"Round {round_num} - Your Attack!")
            print(f"You deal {ph} damage! Enemy HP: {enhp}/{enmaxhp}")
            print(f"XP gained this round: {round_xp}")
            s(0.5)
            
            if enhp <= 0:
                logo()
                print(f"\nVictory! Match {total_matches - matches_remaining + 1} complete!")
                s(1)
                hp = maxhp
                dfn = maxdfn
                matches_remaining -= 1
                break
                
            # Enemy attack
            logo()
            eh = r.randint(int(endmg/2), endmg)
            if eh > dfn:
                actual_damage = eh - dfn
                dfn = max(0, dfn - int(eh * 0.5))  # Defense reduced by half of incoming damage
            else:
                actual_damage = 0
                dfn = max(0, dfn - int(eh * 0.5))  # Defense still reduced even if damage blocked
            hp -= actual_damage
            
            # XP penalty for damage taken
            xp_penalty = int(actual_damage * 0.1)
            round_xp = max(0, round_xp - xp_penalty)
            
            print(f"Round {round_num} - Enemy Attack!")
            print(f"Enemy deals {eh} damage! Your HP: {hp}/{maxhp}")
            print(f"Your Defense: {dfn}/{maxdfn}")
            print(f"XP penalty from damage: {xp_penalty}")
            print(f"Final XP this round: {round_xp}")
            round_num += 1
            save()
            s(0.5)

            if hp <= 0:
                logo()
                print("You've been defeated!")
                s(1)
                savewipe()
                return

    logo()
    print(f"\nAll {total_matches} matches complete! Total XP gained: {gxp}")
    s(1)
    xp += gxp
    while xp >= maxxp:
        xp -= maxxp
        maxxp = int((maxxp * 1.15) + (level * 8.5))
        level += 1
        stp += 1
        print(f"Level up! {stp} Status Points available!")
        s(0.5)
    input("\nPress Enter to continue")
    gamelist()


def savewipe():
    global xp, maxxp, stp, level, dmg, hp, maxhp, dfn, maxdfn, usedheal, useddfn, usedmp, useddmg
    print("Game Over - Save wiped")
    xp = 0
    maxxp = 10
    stp = level = 5
    dmg = 5
    hp = maxhp = 20
    dfn = maxdfn = usedheal = useddfn = usedmp = useddmg = 0
    save()
    hub()

lsn()
