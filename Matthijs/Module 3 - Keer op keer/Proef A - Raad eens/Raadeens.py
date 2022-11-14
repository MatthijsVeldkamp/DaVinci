import random
import os
import time
os.system("cls")
score = 0
randomgetal = random.randint(1,1000)
ronde = 1
aantalkeer = 0
input1 = ("x")
stop = False
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
        os.system("cls")
        while aantalkeer < 11 and score < 20 and stop == False:
            print("Ronde: "+str(ronde)+"\nScore: "+str(score)+"\nZetten "+str(aantalkeer)+"/10"+"\nVorige gok: "+str(input1))
            aantalkeer += 1
            input1 = input("Raad het getal van 1 tot 1000\nU kunt ook stop typen om te stoppen.\n\n\n\n\n? ")
            if input1.lower() == ("stop"):
                stop = True
                os.system("cls")
                print("Doeg :)")
                time.sleep(1)
            elif input1.lower() == ("cheat"):
                aantalkeer -= 1
                os.system("cls")
                print(randomgetal)
                time.sleep(2)
                input1 = ("x")
                time.sleep(2)
                os.system("cls")   
            else:
                verschil = int(input1) - int(randomgetal)
                verschil = str(verschil)
                verschil = verschil.replace("-", "")
                verschil = int(verschil)
                if verschil == (0):
                    if aantalkeer == 1:
                        aantalkeer = 1
                    else:
                        aantalkeer -= 1
                    print("------------------------------------")
                    print("|                                  |")
                    print("|         Goed geraden!            |")
                    print("|                                  |")
                    print("|  Geraden in: "+str(aantalkeer)+" zet(ten).     ")
                    print("|                                  |")
                    print("------------------------------------")
                    score += 1
                    keuze = input("Wilt u nog een keer?\nY/N\n? ")
                    if keuze.lower() == ("y"):
                        aantalkeer = int(0)
                        randomgetal = random.randint(1,1000)
                        ronde += 1
                        input1 = ("x")
                        stop = False
                        os.system("cls")
                        continue
                    else:
                        os.system("cls")
                        print("Doeg :)")
                        time.sleep(1)
                        stop = True
                elif verschil <= 50 and verschil > 20:
                    if int(randomgetal) < int(input1):
                        print("Lager!")
                    else:
                        print("Hoger!")
                    print("Je bent warm.")
                    time.sleep(1)
                    os.system("cls")
                    continue
                elif verschil <= 20:
                    if int(randomgetal) < int(input1):
                        print("Lager!")
                    else:
                        print("Hoger!")
                    print("Je bent heel erg warm.")
                    time.sleep(1)
                    os.system("cls")
                    continue
                else:
                    if int(randomgetal) < int(input1):
                        print("Lager!")
                    else:
                        print("Hoger!")
                    time.sleep(1)
                    os.system("cls")
                    continue
        else:
            if stop == True:
                break
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
                    aantalkeer = 0
                    randomgetal = random.randint(1,1000)
                    ronde += int(1)
                    input1 = ("x")
                    os.system("cls")
                    score = 0
                    continue
                else:
                    os.system("cls")
                    print("Doeg :)")
                    time.sleep(1)
                    break
            
    except:
        print("Type A.U.B alleen nummers of stop.")
        input1 = "x"
        time.sleep(2)