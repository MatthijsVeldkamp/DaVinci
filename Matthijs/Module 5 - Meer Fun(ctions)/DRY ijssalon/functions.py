from foutmeldingen import *
from prijzen import *
import os
import time
from termcolor import colored
import math
bestelling = {'Bolletjes': 0,
              'Bakjes': 0,
              'Hoorntjes': 0}
aantalbolletjes = 0
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
        print(f"Hier is uw bakje met {hoeveel} bolletjes.")
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
welkesmaken = ["chocola", "aardbei", "munt", "mokka", "walnoot","vanille","meloen","banaan"]
smaken = []
def smaakkeuze(aantalbolletjes):
    for aantalbolletjes in range(aantalbolletjes):
        while True:
            smaak = input(f"Welke smaak wilt u voor bolletje {aantalbolletjes+1}? ").lower()
            # checken of de smaak in de lijst welkesmaken staat
            if smaak in welkesmaken:
                smaken.append(smaak)
                break
            else:
                print("Sorry, die smaak hebben we niet.")
                aantalbolletjes - 1
                continue
def kassabon(hoeveel, verpakking):
    deprijs = bestelling["Bolletjes"] * bolletje
    prijsbakje = bestelling["Bakjes"] * bakje
    prijshoorntje = bestelling["Hoorntjes"] * hoorntje
    totaalprijs = (deprijs + prijsbakje) + (prijshoorntje)
    os.system("cls")
    print('---------["Papi Gelato"]---------')
    print(f"Bolletjes: {bestelling['Bolletjes']}x {bolletje:.2f}       = {deprijs:.2f} euro")
    if bestelling["Bakjes"] != 0:
        print(f"Bakjes: {bestelling['Bakjes']}x {bakje:.2f}          = {prijsbakje:.2f} euro")
    if bestelling["Hoorntjes"] != 0:
        print(f"Hoorntjes: {bestelling['Hoorntjes']}x {hoorntje:.2f}       = {prijshoorntje:.2f} euro")
    print(f"---------------------------------")
    print(f"Totaal:                    {totaalprijs:.2f} euro")
    return
def nogeenkeer():
    while True:
        antwoord = input("Wilt u nog een keer bestellen? (y/n) ")
        if antwoord.lower() == "y":
            nogeenkeerbestellen = True
            os.system("cls")
            return nogeenkeerbestellen
        elif antwoord.lower() == "n":
            nogeenkeerbestellen = False
            os.system("cls")
            return nogeenkeerbestellen
        else:
            nogeenkeerbestellen = ""
            datsnapikniet()
            time.sleep(1.5)
            os.system("cls")
            continue