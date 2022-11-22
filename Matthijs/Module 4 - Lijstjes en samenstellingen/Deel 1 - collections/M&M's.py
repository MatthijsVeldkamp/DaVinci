import random
import time
import os

os.system("cls")
kleuren = ("oranje", "blauw", "groen", "bruin")
zak = []
print("Hoeveel M&M's wilt u?")
try:
    hoeveelheid = int(input("? "))
    for i in range(hoeveelheid):
        zak.append(random.choice(kleuren))
    zak = str(zak)
    zak = zak.replace("[", "")
    zak = zak.replace("]", "")
    zak = zak.replace("'", "")
    print("In de zak zitten M&M's met de kleuren: " + (zak))
except:
    os.system("cls")
    print("Vul alleen nummers in!")
    time.sleep(2)
    os.system("cls")
