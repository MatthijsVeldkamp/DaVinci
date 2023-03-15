from functions import *
from foutmeldingen import *
from prijzen import *
from termcolor import colored
welkom()
hoeveel = hoeveelbolletjes()
welkeverpakking = verpakkingcheck(hoeveel)
if welkeverpakking == "keuze":
    welkeverpakking = verpakking(hoeveel)
kassabon(hoeveel, welkeverpakking)