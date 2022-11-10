import random
import os
import time
os.system("cls")
score = int(0)
randomgetal = random.randint(1,1000)
ronde = int(1)
aantalkeer = int(0)
input1 = ("x")
print("------------------------------------")
print("|                                  |")
print("|           Raadeens.py            |")
print("|                                  |")
print("|  Raad het getal van 1 tot 1000   |")
print("|      U krijgt 10 zetten          |")
print("|                                  |")
print("|                                  |")
print("------------------------------------")
time.sleep(5)
os.system("cls")
while True:    
    try:
        while aantalkeer < 10 and score < 20:
            print("Ronde: "+str(ronde)+"\nScore: "+str(score)+"\nAantal keer geraden: "+str(aantalkeer)+"\nVorige gok: "+str(input1))
            print(randomgetal)
            input1 = input("Raad het getal van 1 tot 1000\nU kunt ook stop typen om te stoppen.\n\n\n\n\n? ")
            
            if input1.lower() == ("stop"):
                break   
            else:
                verschil = int(input1) - int(randomgetal)
                verschil = str(verschil)
                verschil = verschil.replace("-", "")
                verschil = int(verschil)
                
                if verschil == (0):
                    print("------------------------------------")
                    print("|                                  |")
                    print("|         Goed geraden!            |")
                    print("|                                  |")
                    print("|  Geraden in: "+str(aantalkeer)+" zetten.     ")
                    print("|                                  |")
                    print("------------------------------------")
                    score += 1
                    keuze = input("Wilt u nog een keer?\nY/N\n? ")
                    if keuze.lower() == ("y"):
                        aantalkeer = int(0)
                        randomgetal = random.randint(1,1000)
                        ronde += int(1)
                        input1 = ("x")
                        os.system("cls")
                        continue
                    else:
                        os.system("cls")
                        break
                elif verschil <= 50 and verschil > 20:
                    if int(randomgetal) < int(input1):
                        print("Lager!")
                    else:
                        print("Hoger!")
                    print("Je bent warm.")
                    time.sleep(1)
                    os.system("cls")
                    aantalkeer += 1
                    continue
                elif verschil <= 20:
                    if int(randomgetal) < int(input1):
                        print("Lager!")
                    else:
                        print("Hoger!")
                    print("Je bent heel erg warm.")
                    time.sleep(1)
                    os.system("cls")
                    aantalkeer += 1
                    continue
                else:
                    if int(randomgetal) < int(input1):
                        print("Lager!")
                    else:
                        print("Hoger!")
                    time.sleep(1)
                    aantalkeer += 1
                    os.system("cls")
                    continue
        else:
            print("------------------------------------")
            print("|                                  |")
            print("|             Helaas!              |")
            print("|     U heeft geen zetten meer!    |")
            print("|      Eindscore: "+str(score)+".   ")
            print("|                                  |")
            print("------------------------------------")
            time.sleep(2)
            keuze = input("Wilt u nog een keer?\nY/N\n? ")
            if keuze.lower() == ("y"):
                aantalkeer = int(0)
                randomgetal = random.randint(1,1000)
                ronde += int(1)
                input1 = ("x")
                os.system("cls")
                continue
            else:
                os.system("cls")
                break
            
    except:
        print("Type A.U.B alleen nummers of stop.")
        time.sleep(2)