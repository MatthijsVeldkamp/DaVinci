import time
import os
import random
namen = []
lootjes = []
loop = True
while True:
    os.system('cls')
    while loop == True:
        try:
            aantal = int(input ("Wat is het aantal deelnemers? "))
            if aantal >=3:
                loop = False
            else:
                print("A.u.b een minimum van 3 deelnemers!")
                time.sleep(2)
                loop = True
        except:
            print ("A.u.b alleen cijfers!!")
            time.sleep(2)
            loop = True
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
        loop = True
        namen.clear()
        continue
    else:
        os.system("cls")
        laasteinlijst = len(namen)
        laasteinlijst -= 1
        b = 0
        print("Lootjes worden gegenereerd...")
        random.shuffle(namen)
        time.sleep(0.5)
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
        break