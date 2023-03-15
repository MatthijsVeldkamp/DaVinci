from foutmeldingen import *
from prijzen import *
import os
import time
from termcolor import colored
<<<<<<< HEAD
import math
aantalbolletjes = 0
=======
vanilleprijs = 1.20
>>>>>>> f2610b512ef220d619410c9f0686c233fbfad8fb
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
<<<<<<< HEAD
def kassabon(hoeveel, verpakking):
    if verpakking == "bakje":
        deprijs = hoeveel * bolletje
        prijsbakje = hoeveel * bakje
        totaalprijs = deprijs + prijsbakje
        print('---------["Papi Gelato"]---------')
        print(f"Bolletjes: {hoeveel}x {bolletje:.2f} euro = {deprijs:.2f} euro")
        print(f"{verpakking}:     1x {bakje:.2f} euro")
        print(f"                         -------")
        print(f"                  Totaal: {totaalprijs:.2f} euro")
    else:
        print(f"Dan krijgt u van mij een hoorntje met {hoeveel} bolletje(s).")
=======
def prijsberekening(hoeveel):
    deprijs = hoeveel * vanilleprijs
    return format(deprijs,'.2f') 
def kassabon(hoeveel, verpakking,prijs):
    print(f"Dan krijgt u van mij een {verpakking} met {hoeveel} bolletje(s).\nDat kost in totaal € {prijs}.")
>>>>>>> f2610b512ef220d619410c9f0686c233fbfad8fb
