import os
import time
boodschappenlijstje = {
}
hoeveel = int(0)
while True:
    os.system("cls")
    product = input("Wat wilt u toevoegen? ")
    productlower = product.lower()
    if productlower not in boodschappenlijstje:
        hoeveel = input("Hoeveel keer? ")
        boodschappenlijstje[productlower] = hoeveel
        input1 = input("Wilt u nog wat toevoegen? ")
        if input1.lower() == ("y") or input1.lower() == ("ja") or input1.lower() == ("yes") or input1.lower() == ("j"):
            continue
        elif input1.lower() == ("n") or input1.lower() == ("nee") or input1.lower() == ("no"):
            os.system("cls")
            print("Boodschappenlijstje:\n")
            for key,value in boodschappenlijstje.items():
                print(key+": "+value+"x")
            break
    else:
            hoeveel = int(input("Hoeveel keer? "))
            boodschappenlijstje[productlower] = int(hoeveel)
            input1 = input("Wilt u nog wat toevoegen? ")
            if input1.lower() == ("y") or input1.lower() == ("ja") or input1.lower() == ("yes") or input1.lower() == ("j"):
                continue
            elif input1.lower() == ("n") or input1.lower() == ("nee") or input1.lower() == ("no"):
                os.system("cls")
                print("Boodschappenlijstje:\n")
                for key,value in boodschappenlijstje.items():
                    print(key+": "+value+"x")
                break