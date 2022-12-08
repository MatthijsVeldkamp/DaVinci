import random
import time
import os
from slprint.slowprint import slowprint
loop = True
def add_to_inventory(item:str):
    inventory.append(item)
def remove_from_inventory(item:str):
    inventory.remove(item)
inventory = []
key = False
while loop == True:
    os.system("cls")
    slowprint ("A: Search.\n", delay = 0.03)
    slowprint ("B: Escape.\n", delay = 0.03)
    slowprint ("C: Check your inventory.\n", delay = 0.03)
    slowprint ("D: Stop the game.\n", delay = 0.03)
    input1 = input("What do you want to do? ")
    if input1.lower() == ("a"):
        os.system("cls")
        slowprint("Searching for items.\n", delay = 0.03)
        time.sleep(1)
        os.system("cls")
        print("Searching for items..\n")
        time.sleep(1)
        os.system("cls")
        print("Searching for items...\n")
        time.sleep(1)
        os.system("cls")
        print("You found a key!\n")
        add_to_inventory("Key for a door.")
        key = True
        time.sleep(2)
        os.system("cls")
        slowprint("The key has been added to your inventory!\n", delay = 0.03)
        time.sleep(2)
        continue
    elif input1.lower() == ("b"):
        os.system("cls")
        slowprint("You aproach a door.\n", delay = 0.03)
        time.sleep(1)
        if key == False:
            slowprint("You don't have any keys to open a door...\n", delay = 0.03)
            time.sleep(1)
        else:
            slowprint("You open the door using the key that you found.\n", delay = 0.03)
            try:
                remove_from_inventory("Key for a door.")
            except:
                pass
            time.sleep(1)
            slowprint("You escaped.\n", delay = 0.03)
        time.sleep(2)
        continue
    elif input1.lower() == ("c"):
        if len(inventory) == (0):
            os.system("cls")
            slowprint("There are no items in your inventory at this moment...\n", delay = 0.03)
            time.sleep(2)
        else:
            os.system("cls")
            slowprint("Items in your inventory:\n", delay = 0.03)
            for i in range(len(inventory)):
                slowprint(inventory[i], delay = 0.03)
            print("\n")
            time.sleep(3)
    elif input1.lower() == ("d"):
        os.system("cls")
        break