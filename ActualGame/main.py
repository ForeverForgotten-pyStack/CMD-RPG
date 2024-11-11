import time, os, sys
from os import system, name

# Renaming of the ones used most often
from time import sleep as s
import random as r

#Clears all variables on start (defines them)
userinp = 0
randamt = 0


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
    pass

def signup():
    pass

def save():
    pass

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


