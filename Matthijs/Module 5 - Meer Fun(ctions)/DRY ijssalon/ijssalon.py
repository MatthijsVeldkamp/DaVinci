from functions import *
from foutmeldingen import *
from termcolor import colored
welkom()
hoeveel = hoeveelbolletjes()
welkeverpakking = verpakkingcheck(hoeveel)
if welkeverpakking == "keuze":
    welkeverpakking = verpakking(hoeveel)
deprijs = prijsberekening(hoeveel)
kassabon(hoeveel, welkeverpakking,deprijs)