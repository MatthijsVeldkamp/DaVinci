from functions import *
from foutmeldingen import *
from prijzen import *
from termcolor import colored
toppings = []
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
    topping = toppingkeuze(hoeveel, welkeverpakking)
    toppings.append(topping)
    nogeens = nogeenkeer()
    if nogeens == True:
        continue
    else:
        count3()
        kassabon(hoeveel, welkeverpakking,toppings)
        print(colored("Bedankt en tot ziens!","cyan"))
        break