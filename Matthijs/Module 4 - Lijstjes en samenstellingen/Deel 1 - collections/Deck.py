import random
import os
import time
os.system("cls")
speciaal = ("harten","ruiten","klaveren","schoppen")
kaarten = ("2","3","4","5","6","7","8","9","10","boer","vrouw","heer","aas")
deck = []
nummer = 0
nummer1 = 1
nummer2 = 0
score = 0
spelerskaarten = []
randomgetal2 = (random.randint(0, 3))
randomgetal = (random.randint(0, 12))
beginkaart = []
beginkaart.append(speciaal[randomgetal2])
beginkaart.append(kaarten[randomgetal])
beginkaart = str(beginkaart)
beginkaart = beginkaart.replace("[", "")
beginkaart = beginkaart.replace("]", "")
beginkaart = beginkaart.replace(",", "")
beginkaart = beginkaart.replace("'", "")
while True:
    os.system("cls")
    hoeveelkaarten = int(input("Met hoeveel kaarten wilt u spelen?\n? "))
    if hoeveelkaarten > 30:
        print("Dat zijn teveel kaarten!")
        time.sleep(2)
    else:
        os.system("cls")
        for i in range(4):
            for i in range (13):
                deck.append(speciaal[nummer]+ " " + kaarten[i])
            nummer += 1
        for i in range(2):
            deck.append("joker")
        random.shuffle(deck)
        for i in range(hoeveelkaarten):
            spelerskaarten.append(deck[nummer2])
            nummer1 += 1
            nummer2 += 1
        while True:
            if len(spelerskaarten) == 1:
                print("Laatste kaart!!!")
            elif len(spelerskaarten) == 0:
                print("U heeft alle kaarten weggespeelt!!!")
                time.sleep(2)
                break
            if beginkaart in spelerskaarten:
                randomgetal2 = (random.randint(0, 3))
                randomgetal = (random.randint(0, 12))
                beginkaart = []
                beginkaart.append(speciaal[randomgetal2])
                beginkaart.append(kaarten[randomgetal])
                beginkaart = str(beginkaart)
                beginkaart = beginkaart.replace("[", "")
                beginkaart = beginkaart.replace("]", "")
                beginkaart = beginkaart.replace(",", "")
                beginkaart = beginkaart.replace("'", "")
            else:
                print("Uw kaarten:",str(len(spelerskaarten))+"\n"+str(spelerskaarten))
                print("Op het spel ligt een",beginkaart+".")
                welkekaart = input("Welke kaart wilt u wegspelen?\n? ")
                try:
                    if beginkaart == "joker":
                        print("U speelt de",welkekaart,"weg!")
                        spelerskaarten.remove(welkekaart)
                        beginkaart = welkekaart
                        time.sleep(1)
                        os.system("cls")
                        continue
                    elif welkekaart == "joker":
                        if "joker" in spelerskaarten:
                            print("U speelt de",welkekaart,"weg!")
                            spelerskaarten.remove(welkekaart)
                            beginkaart = welkekaart
                            time.sleep(1)
                            os.system("cls")
                            continue
                        else:
                            print("U heeft geen",welkekaart+"!")
                            time.sleep(1)
                            os.system("cls")
                            continue
                    elif welkekaart == "kaart pakken":
                        print("Kaart pakken!")
                        jokerkans = (random.randint(12,25))
                        if jokerkans == 25:
                            kaartpakken = ["joker"]
                            kaartpakken = str(kaartpakken)
                            kaartpakken = kaartpakken.replace("[", "")
                            kaartpakken = kaartpakken.replace("]", "")
                            kaartpakken = kaartpakken.replace(",", "")
                            kaartpakken = kaartpakken.replace("'", "")
                            spelerskaarten.append(kaartpakken)
                            time.sleep(1)
                            os.system("cls")
                            continue
                        else:
                            opnieuw = True
                            while opnieuw == True:
                                randomgetal4 = (random.randint(0, 3))
                                randomgetal3 = (random.randint(0, 12))
                                kaartpakken = []
                                kaartpakken.append(speciaal[randomgetal4])
                                kaartpakken.append(kaarten[randomgetal3])
                                kaartpakken = str(kaartpakken)
                                kaartpakken = kaartpakken.replace("[", "")
                                kaartpakken = kaartpakken.replace("]", "")
                                kaartpakken = kaartpakken.replace(",", "")
                                kaartpakken = kaartpakken.replace("'", "")
                                if kaartpakken in spelerskaarten or kaartpakken in beginkaart:
                                    continue
                                else:
                                    opnieuw = False
                                    spelerskaarten.append(kaartpakken)
                                    time.sleep(1)
                                    os.system("cls")
                                    continue
                    elif (welkekaart.split(' ', 1)[1]) == (beginkaart.split(' ', 1)[1]):
                        if welkekaart in spelerskaarten:
                            print("U speelt de",welkekaart,"weg!")
                            spelerskaarten.remove(welkekaart)
                            beginkaart = welkekaart
                            time.sleep(1)
                            os.system("cls")
                            continue
                        else:
                            print("U heeft geen",welkekaart+"!")
                            time.sleep(1)
                            os.system("cls")
                            continue
                    elif (welkekaart.split(' ', 1)[0]) == (beginkaart.split(' ', 1)[0]):
                        if welkekaart in spelerskaarten:
                            print("U speelt de",welkekaart,"weg!")
                            spelerskaarten.remove(welkekaart)
                            beginkaart = welkekaart
                            time.sleep(1)
                            os.system("cls")
                            continue
                        else:
                            print("U heeft geen",welkekaart+"!")
                            time.sleep(1)
                            os.system("cls")
                            continue
                    elif welkekaart == "joker":
                        print("U speelt de",welkekaart,"weg!")
                        spelerskaarten.remove(welkekaart)
                        beginkaart = welkekaart
                        time.sleep(1)
                        os.system("cls")
                        continue
                    else:
                        print("Actie niet toegelaten!")
                        time.sleep(1)
                        os.system("cls")
                        continue
                except:
                    print("Er ging iets fout!")
                    time.sleep(2)
                    os.system("cls")
                    continue
        break
