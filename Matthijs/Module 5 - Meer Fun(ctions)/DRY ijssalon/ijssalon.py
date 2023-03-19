from functions import *
from foutmeldingen import *
from prijzen import *
from termcolor import colored
welkom()
def addtobestelling():
    if welkeverpakking == "bakje":
            bestelling['Bakjes'] += 1
    elif welkeverpakking == "hoorntje":
        bestelling['Hoorntjes'] += 1
while True:
    hoeveel = hoeveelbolletjes()
    aantalbolletjes = hoeveel
    bestelling['Bolletjes'] += int(hoeveel)
    welkeverpakking = verpakkingcheck(hoeveel)
    if welkeverpakking == "keuze":
        welkeverpakking = verpakking(hoeveel)
    smaakkeuze(aantalbolletjes)
    addtobestelling()
    nogeens = nogeenkeer()
    if nogeens == True:
        continue
    else:
        kassabon(hoeveel, welkeverpakking)
        print(colored("Bedankt en tot ziens!","cyan"))
        for aantalbolletjes in range(aantalbolletjes):
            print(f"bolletje {aantalbolletjes+1}: {smaken[aantalbolletjes]}")
        break