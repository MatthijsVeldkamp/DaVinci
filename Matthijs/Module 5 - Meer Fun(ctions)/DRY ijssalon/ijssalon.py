from functions import *
from foutmeldingen import *
from prijzen import *
from termcolor import colored
welkom()
while True:
    hoeveel = hoeveelbolletjes()
    welkeverpakking = verpakkingcheck(hoeveel)
    if welkeverpakking == "keuze":
        welkeverpakking = verpakking(hoeveel)
    kassabon(hoeveel, welkeverpakking)
    nogeens = nogeenkeer()
    if nogeens == True:
        continue
    else:
        print(colored("Bedankt en tot ziens!","cyan"))
        break