import os
import time
loop = True
opnieuw = True
os.system("cls")
# -------------------------------------------------------
def addition(n1: float, n2: float) -> float:
    totaal = n1 + n2
    return totaal
# -------------------------------------------------------
def subtraction(n1: float, n2: float) -> float:
    totaal = n1 - n2
    return totaal
# -------------------------------------------------------
def multiplication(n1: float, n2: float) -> float:
    totaal = n1 * n2
    return totaal
# -------------------------------------------------------
def division(n1: float, n2: float) -> float:
    totaal = n1 / n2
    return totaal
# -------------------------------------------------------
while opnieuw == True:
    os.system("cls")
    print ("|-=+=--=+=--=+=--=+=--=+=--=+=--=+=-|")
    print ("| A) getallen optellen              |")
    print ("| B) getallen aftrekken             |")
    print ("| C) getallen vermenigvuldigen      |")
    print ("| D) getallen delen                 |")
    print ("| E) getal ophogen                  |")
    print ("| F) getal verlagen                 |")
    print ("| G) getal verdubbelen              |")
    print ("| H) getal halveren                 |")
    print ("|-=+=--=+=--=+=--=+=--=+=--=+=--=+=-|")

    choice = input("Wat wilt u doen? ")
    # ------------------------------------------------------- 
    if choice.lower() == "a":
        try:
            n1= float(input("Getal 1?  "))
        except:
            print("NaN!")
            time.sleep(2)
            continue
        try:
            n2 = float(input("Hoeveel wilt u erbij doen? "))
        except:
            print("NaN!")
            time.sleep(2)
            continue
        totaal = addition(n1, n2)
        print (f"{n1} + {n2} = {totaal}")
        time.sleep(2)
        opnieuw = False
    # ------------------------------------------------------- 
    elif choice.lower() == "b":
        try:
            n1= float(input("Getal 1: "))
        except:
            print("NaN!")
            time.sleep(2)
            continue
        try:
            n2 = float(input("Hoeveel wilt u eraf halen? "))
        except:
            print("NaN!")
            time.sleep(2)
            continue
        totaal = subtraction(n1, n2)
        print (f"{n1} - {n2} = {totaal}")
        time.sleep(2)
        opnieuw = False
    # ------------------------------------------------------- 
    elif choice.lower() == "c":
        try:
            n1= float(input("Getal 1: "))
        except:
            print("NaN!")
            time.sleep(2)
            continue
        try:
            n2 = float(input("Met hoeveel wilt u keren? "))
        except:
            print("NaN!")
            time.sleep(2)
            continue
        totaal = multiplication(n1, n2)
        print (f"{n1} x {n2} = {totaal}")
        time.sleep(2)
        opnieuw = False
    # ------------------------------------------------------- 
    elif choice.lower() == "d":
        try:
            n1= float(input("Getal 1: "))
        except:
            print("NaN!")
            time.sleep(2)
            continue
        try:
            n2 = float(input("Met hoeveel wilt u delen? "))
        except:
            print("NaN!")
            time.sleep(2)
            continue
        totaal = division(n1, n2)
        print (f"{n1} : {n2} = {totaal}")
        time.sleep(2)
        opnieuw = False
    # ------------------------------------------------------- 
    elif choice.lower() == "e":
        try:
            n1= float(input("Welk getal wilt u ophogen? "))
        except:
            print("NaN!")
            time.sleep(2)
            continue
        n2= 1
        totaal = addition(n1, n2)
        print (f"{n1} + {n2} = {totaal}")
        time.sleep(2)
        opnieuw = False
    # ------------------------------------------------------- 
    elif choice.lower() == "f":
        try:
            n1= float(input("Welk getal wilt u verlagen? "))
        except:
            print("NaN!")
            time.sleep(2)
            continue
        n2= 1
        totaal = subtraction(n1, n2)
        print (f"{n1} - {n2} = {totaal}")
        time.sleep(2)
        opnieuw = False
    # ------------------------------------------------------- 
    elif choice.lower() == "g":
        try:
            n1= float(input("Welk getal wilt u verdubbelen? "))
        except:
            print("NaN!")
            time.sleep(2)
            continue
        n2= 2
        totaal = multiplication(n1, n2)
        print (f"{n1} x {n2} = {totaal}")
        time.sleep(2)
        opnieuw = False
    # ------------------------------------------------------- 
    elif choice.lower() == "h":
        try:
            n1= float(input("Welk getal wilt u halveren? "))
        except:
            print("NaN!")
            time.sleep(2)
            continue
        n2 = 2
        totaal = division(n1, n2)
        print (f"{n1} : {n2} = {totaal}")
        time.sleep(2)
        opnieuw = False
    # --------------------------------------------------------
    else:
        print("Dat was geen optie!")
        time.sleep(2)
    #---------------------------------------------------------
while loop == True:
    os.system("cls")
    print("Wat wilt u doen met het vorige getal?","("+str(totaal)+")")
    print ("|-=+=--=+=--=+=--=+=--=+=--=+=--=+=-|")
    print ("| A) getallen optellen              |")
    print ("| B) getallen aftrekken             |")
    print ("| C) getallen vermenigvuldigen      |")
    print ("| D) getallen delen                 |")
    print ("| E) getal ophogen                  |")
    print ("| F) getal verlagen                 |")
    print ("| G) getal verdubbelen              |")
    print ("| H) getal halveren                 |")
    print ("| I) niks (Eindantwoord printen)    |")
    print ("|-=+=--=+=--=+=--=+=--=+=--=+=--=+=-|")
    choice = input("Wat wilt u doen? ")
    # ------------------------------------------------------- 
    if choice.lower() == "a":#optellen
        n1 = totaal
        try:
            n2 = float(input("Hoeveel wilt u erbij doen? "))
        except:
            print("NaN!")
            time.sleep(2)
            continue
        totaal = addition(n1, n2)
        print (f"{n1} + {n2} = {totaal}")
        time.sleep(2)
    # ------------------------------------------------------- 
    elif choice.lower() == "b":#aftrekken
        n1 = totaal
        try:
            n2 = float(input("Hoeveel wilt u eraf halen? "))
        except:
            print("NaN!")
            time.sleep(2)
            continue
        totaal = subtraction(n1, n2)
        print (f"{n1} - {n2} = {totaal}")
        time.sleep(2)
    # ------------------------------------------------------- 
    elif choice.lower() == "c":#vermenigvuldigen
        n1 = totaal
        try:
            n2 = float(input("Met hoeveel wilt u keren? "))
        except:
            print("NaN!")
            time.sleep(2)
            continue
        totaal = multiplication(n1, n2)
        print (f"{n1} x {n2} = {totaal}")
        time.sleep(2)
    # ------------------------------------------------------- 
    elif choice.lower() == "d":#delen
        n1 = totaal
        try:
            n2 = float(input("Met hoeveel wilt u delen? "))
        except:
            print("NaN!")
            time.sleep(2)
            continue
        totaal = division(n1, n2)
        print (f"{n1} : {n2} = {totaal}")
        time.sleep(2)
    # ------------------------------------------------------- 
    elif choice.lower() == "e":#ophogen
        n1 = totaal
        n2= 1
        totaal = addition(n1, n2)
        print (f"{n1} + {n2} = {totaal}")
        time.sleep(2)
    # ------------------------------------------------------- 
    elif choice.lower() == "f":#verlagen
        n1 = totaal
        n2 = 1
        totaal = subtraction(n1, n2)
        print (f"{n1} - {n2} = {totaal}")
        time.sleep(2)
    # ------------------------------------------------------- 
    elif choice.lower() == "g":#verdubbelen
        n1 = totaal
        n2= 2
        totaal = multiplication(n1, n2)
        print (f"{n1} x {n2} = {totaal}")
        time.sleep(2)
    # ------------------------------------------------------- 
    elif choice.lower() == "h":#halveren
        n1 = totaal
        n2 = 2
        totaal = division(n1, n2)
        print (f"{n1} : {n2} = {totaal}")
        time.sleep(2)
    # -------------------------------------------------------
    elif choice.lower() == ("i"):#niks
        loop = False
        continue
    else:
        print("Dat was geen optie!")
        time.sleep(2)
else:    
    print("Het eindresultaat is:",totaal)