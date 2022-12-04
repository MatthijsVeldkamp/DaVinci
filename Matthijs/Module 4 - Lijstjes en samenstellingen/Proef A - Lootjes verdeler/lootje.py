import time
import os
import random
i = 0
a = 0
b = 0
namen = []
lootjes = []
naamloop = True
while True:
    os.system('cls')
    while naamloop == True:
        try:
            aantal = int(input ("Wat is het aantal deelnemers? "))
            if aantal >=3:
                naamloop = False
            else:
                print("A.u.b een minimum van 3 deelnemers!")
                time.sleep(2)
                naamloop = True
        except:
            print ("Dat is een woord! geen cijfer")
            time.sleep(2)
            naamloop = True
    hoeveelheidloop = aantal
    while hoeveelheidloop >0:
        os.system("cls")
        print ("Nog toevoegen: ",hoeveelheidloop)
        naam = input("Wie wilt u toevoegen? ").lower()
        if naam.lower() in namen:
            print("Die persoon staat al in de lijst!")
            time.sleep(2)
            continue
        else:
            namen.append(naam)
            hoeveelheidloop -=1
            pass
    os.system("cls")
    print(namen)
    input1 = input("Klopt dit? ")
    if input1.lower() == ("n"):
        naamloop = True
        namen.clear()
        continue
    else:
        laasteinlijst = len(namen)
        laasteinlijst -= 1
        b = 0
        print("Lootjes worden gegenereerd...")
        random.shuffle(namen)
        time.sleep(1.25)
        while b < laasteinlijst:
            lootje = (namen[b],"heeft",namen[b+1])
            lootjes.append(lootje)
            b +=1
        else:
            laatste = (namen[laasteinlijst]," heeft ",namen[0])
            lootjes.append(laatste)
        lootjes = str(lootjes)
        lootjes = lootjes.replace("[", "")
        lootjes = lootjes.replace("]", "")
        lootjes = lootjes.replace("'", "")
        print (lootjes)
        print("Druk op Ctrl + C om te stoppen.")
        while True:
            time.sleep(1)
            continue