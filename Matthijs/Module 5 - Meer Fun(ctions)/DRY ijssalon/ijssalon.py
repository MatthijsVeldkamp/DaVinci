from functions import *
from foutmeldingen import *
from prijzen import *
from termcolor import colored
toppings = []
welkom()
welkeklant = particulierofzakelijk()
if welkeklant == "particulier":
    while True:
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
            kassabonparticulier(hoeveel, welkeverpakking,toppings)
            print(colored("Bedankt en tot ziens!","cyan"))
            break
else:
    while True:
        hoeveel = hoeveelliter()
        aantalliters = hoeveel
        bestelling['Bolletjes'] += int(hoeveel)
        smaakkeuzezakelijk(aantalliters)
        addtobestelling("bakje")
        nogeens = nogeenkeer()
        if nogeens == True:
            continue
        else:
            count3()
            kassabonzakelijk(hoeveel)
            print(colored("Bedankt en tot ziens!","cyan"))
            break