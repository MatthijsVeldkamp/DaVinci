from functions import *
from foutmeldingen import *
from prijzen import *
from termcolor import colored
toppings = []
welkom()
while True:
    welkeklant = particulierofzakelijk()
    if welkeklant == "particulier":
        hoeveel = hoeveelbolletjes()
        aantalbolletjes = hoeveel
        bestelling['Bolletjes'] += int(hoeveel)
        welkeverpakking = verpakkingcheck(hoeveel)
        if welkeverpakking == "keuze":
            welkeverpakking = verpakking(hoeveel)
        smaakkeuze(aantalbolletjes)
        addtobestelling(welkeverpakking)
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
    else:
        hoeveel = hoeveelliter()
        aantalbolletjes = hoeveel
        bestelling['Bolletjes'] += int(hoeveel)
        welkeverpakking = verpakkingcheck(hoeveel)
        if welkeverpakking == "keuze":
            welkeverpakking = verpakking(hoeveel)
        smaakkeuze(aantalbolletjes)
        addtobestelling(welkeverpakking)
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