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
def particulierofzakelijk():
    while True:
        print(colored("Bent u 1) particulier of 2) zakelijk?","cyan"))
        welkeklant = input("? ").lower()
        if welkeklant == "1":
            return "particulier"
        elif welkeklant == "2":
            return "zakelijk"
        else:
            datsnapikniet()
            time.sleep(1.5)
            os.system("cls")
            continue
def welkom():
    os.system("cls")
    print("Welkom bij Papi Gelatto!")
def hoeveelliter():
    while True:
        print(colored("Hoeveel liter wilt u?","cyan"))
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
def addtobestelling(welkeverpakking):
    if welkeverpakking == "bakje":
            bestelling['Bakjes'] += 1
    elif welkeverpakking == "hoorntje":
        bestelling['Hoorntjes'] += 1
def verpakkingcheck(hoeveel):
    if hoeveel >= 4 and hoeveel <=8:
        print(f"Hier is uw bakje met {hoeveel} bolletjes.")
        time.sleep(2)
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
welkesmaken = ["c", "a","v","m"]
smaken = []
aantalsmaken = []
count2 = []
def toppingkeuze(hoeveel, welkeverpakking):
    welketopping = input("Welke topping wilt u?\nU kunt kiezen uit: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus.\n? ").lower()
    if welketopping == "a":
        print("U heeft geen topping gekozen.")
        time.sleep(2)
        return
    elif welketopping == "b":
        return "slagroom"
    elif welketopping == "c":
        return "sprinkels"
    elif welketopping == "d":
        return "caramel"
    else:
        datsnapikniet()
        time.sleep(1.5)
        os.system("cls")
        toppingkeuze()
def smaakkeuze(aantalbolletjes):
    for aantalbolletjes in range(aantalbolletjes):
        while True:
            os.system("cls")
            smaak = input(f"Welke smaak wilt u voor bolletje {aantalbolletjes+1}\nU kunt kiezen uit: (c)hocola, (a)ardbei, (v)anille of (m)unt.\n? ").lower()
            # checken of de smaak in de lijst welkesmaken staat
            if smaak in welkesmaken:
                smaken.append(smaak)
                break
            else:
                print("Sorry, die smaak hebben we niet.")
                aantalbolletjes - 1
                time.sleep(1.5)
                continue
def smaakkeuzezakelijk(aantalbolletjes):
    while True:
        os.system("cls")
        smaak = input(f"Welke smaak wilt u?\nU kunt kiezen uit: (c)hocola, (a)ardbei, (v)anille of (m)unt.\n? ").lower()
        # checken of de smaak in de lijst welkesmaken staat
        if smaak in welkesmaken:
            for aantalbolletjes in range(aantalbolletjes):
                smaken.append(smaak)
            break
        else:
            print("Sorry, die smaak hebben we niet.")
            aantalbolletjes - 1
            time.sleep(1.5)
            continue
def count3():
    countsmaak = smaken.count("c")
    count2.append(countsmaak)
    countsmaak = smaken.count("a")
    count2.append(countsmaak)
    countsmaak = smaken.count("v")
    count2.append(countsmaak)
    countsmaak = smaken.count("m")
    count2.append(countsmaak)
def kassabonparticulier(hoeveel, verpakking,toppings):
    toppingprijs = 0
    for topping in range(len(toppings)):
        if toppings[topping] == "slagroom":
            toppingprijs = toppingprijs + slagroom
        elif toppings[topping] == "sprinkels":
            toppingprijs = toppingprijs + (sprinkels * hoeveel)
        elif toppings[topping] == "caramel":
            if verpakking == "hoorntje":
                toppingprijs = toppingprijs + caramelhoorntje
            elif verpakking == "bakje":
                toppingprijs = toppingprijs + caramelbakje
    deprijs = bestelling["Bolletjes"] * bolletje
    prijsbakje = bestelling["Bakjes"] * bakje
    prijshoorntje = bestelling["Hoorntjes"] * hoorntje
    totaalprijs = (deprijs + prijsbakje) + (prijshoorntje) + toppingprijs
    os.system("cls")
    print('---------["Papi Gelato"]---------')
    if count2[0] != 0:
        print(f"B.Chocola: {count2[0]}x {bolletje:.2f}        = {count2[0] * bolletje:.2f} euro")
    if count2[1] != 0:
        print(f"B.Aardbei: {count2[1]}x {bolletje:.2f}        = {count2[1] * bolletje:.2f} euro")
    if count2[2] != 0:
        print(f"B.Vanille: {count2[2]}x {bolletje:.2f}        = {count2[2] * bolletje:.2f} euro")
    if count2[3] != 0:
        print(f"B.Munt: {count2[3]}x {bolletje:.2f}        = {count2[3] * bolletje:.2f} euro")
    if toppings != [None]:
        print(f"Topping:                 = {toppingprijs:.2f} euro")
    if bestelling["Bakjes"] != 0:
        print(f"Bakjes: {bestelling['Bakjes']}x {bakje:.2f}          = {prijsbakje:.2f} euro")
    if bestelling["Hoorntjes"] != 0:
        print(f"Hoorntjes: {bestelling['Hoorntjes']}x {hoorntje:.2f}       = {prijshoorntje:.2f} euro")
    print(f"---------------------------------")
    print(f"Totaal:                    {totaalprijs:.2f} euro")
    return
def kassabonzakelijk(hoeveel):
    deprijs = bestelling["Bolletjes"] * perliter
    totaalprijs = deprijs
    btw = (totaalprijs / 109) * 100
    os.system("cls")
    print('---------["Papi Gelato"]---------')
    if count2[0] != 0:
        print(f"L.Chocola: {count2[0]}x {perliter:.2f}        = {count2[0] * perliter:.2f} euro")
    if count2[1] != 0:
        print(f"L.Aardbei: {count2[1]}x {perliter:.2f}        = {count2[1] * perliter:.2f} euro")
    if count2[2] != 0:
        print(f"L.Vanille: {count2[2]}x {perliter:.2f}        = {count2[2] * perliter:.2f} euro")
    if count2[3] != 0:
        print(f"L.Munt:    {count2[3]}x {perliter:.2f}        = {count2[3] * perliter:.2f} euro")
    if bestelling["Hoorntjes"] != 0:
        print(f"Hoorntjes: {bestelling['Hoorntjes']}x {hoorntje:.2f}       = {perliter:.2f} euro")
    print(f"---------------------------------")
    print(f"Totaal:                    {totaalprijs:.2f} euro")
    print(f"BTW (9%):             {round((totaalprijs - btw),2)} euro")
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