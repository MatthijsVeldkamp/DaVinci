import time
import os
producten = []
hoeveelheid = []
while True:
    os.system("cls")
    product = input("Welk product wilt u toevoegen?\n? ")
    if (product) in producten:
        os.system("cls")
        print("Dat product staat al in de lijst!")
        time.sleep(2)
    else:
        os.system("cls")
        hoeveelheid1 = input("Hoeveel keer?\n? ")
        producten.append(product)
        hoeveelheid.append(hoeveelheid1)
        os.system("cls")
        input1 = input("Wilt u nog een item toevoegen?\n? ")
        if input1.lower() == ("n") or input1.lower() == ("nee"):
            os.system("cls")
            producten = str(producten)
            producten = producten.replace("[", "")
            producten = producten.replace("]", "")
            producten = producten.replace("'", "")
            hoeveelheid = str(hoeveelheid)
            hoeveelheid = hoeveelheid.replace("[", "")
            hoeveelheid = hoeveelheid.replace("]", "")
            hoeveelheid = hoeveelheid.replace("'", "")
            print("Product: ")
            print("Hoeveelheid: ")
            break
        else:
            continue