import time
import os
lijst = []
aantal = []
a = 0
while True:
    opnieuw = True
    os.system("cls")
    input1 = input("Welk product wilt u toevoegen?\n? ")
    lijst.append(input1)
    nummer = lijst.count(input1)
    if nummer > 1:
        os.system("cls")
        print("Dat product staat al in de lijst!")
        time.sleep(1.5)
        continue
    else:

            input2 = input("Wilt u nog een product toevoegen? Y/N\n? ")
            if input2.lower() == ("n"):
                os.system("cls")
                print(lijst)
                opnieuw = False
                break
            elif input2.lower() == ("y"):
                opnieuw = False
            else:
                os.system("cls")
                print("Dat was geen optie!")
                opnieuw = True
                time.sleep(2)