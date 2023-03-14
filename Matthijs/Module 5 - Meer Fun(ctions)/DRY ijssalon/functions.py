from foutmeldingen import *
import os
import time
from termcolor import colored
vanilleprijs = 1.20
def welkom():
    os.system("cls")
    print("Welkom bij Papi Gelatto, je mag alle smaken kiezen zolang het maar vanille ijs is.")
def hoeveelbolletjes():
    while True:
        print(colored("Hoeveel bolletjes wilt u?","cyan"))
        hoeveel = input("? ")
        try:
            hoeveel = int(hoeveel)
            if hoeveel > 8:
                hebbenweniet()
                time.sleep(1.5)
                os.system("cls")
                welkom()
                continue
            elif hoeveel < 1:
                minimaaleen()
                time.sleep(1.5)
                os.system("cls")
                continue
            else:
                return hoeveel
        except:
            datsnapikniet()
            time.sleep(1.5)
            os.system("cls")
            welkom()
            continue
def verpakkingcheck(hoeveel):
    if hoeveel >= 4 and hoeveel <=8:
        return "bakje"
    elif hoeveel >= 1:
        return "keuze"
def verpakking(hoeveel):
    while True:
        print(colored(f"Wilt u deze {hoeveel} bolletje(s) in een hoorntje of in een bakje?","cyan"))
        welkeverpakking = input("? ")
        if welkeverpakking.lower() == "bakje":
            return "bakje"
        elif welkeverpakking.lower() == "hoorntje":
            return "hoorntje"
        else:
            datsnapikniet()
            time.sleep(1.5)
            os.system("cls")
            continue
def prijsberekening(hoeveel):
    deprijs = hoeveel * vanilleprijs
    return format(deprijs,'.2f') 
def kassabon(hoeveel, verpakking,prijs):
    print(f"Dan krijgt u van mij een {verpakking} met {hoeveel} bolletje(s).\nDat kost in totaal € {prijs}.")