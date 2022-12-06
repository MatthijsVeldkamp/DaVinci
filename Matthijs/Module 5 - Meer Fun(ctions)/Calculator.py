import os
rekenmachine = True
os.system("cls")
# -------------------------------------------------------
def addition(n1: float, n2: float) -> float:
    totaal = n1+ n2
    return totaal
# -------------------------------------------------------
def subtraction(n1: float, n2: float) -> float:
    totaal = n1- n2
    return totaal
# -------------------------------------------------------
def multiplication(n1: float, n2: float) -> float:
    totaal = n1* n2
    return totaal
# -------------------------------------------------------
def division(n1: float, n2: float) -> float:
    totaal = n1/ n2
    return totaal
# -------------------------------------------------------

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
    n1= float(input("Getal 1: "))
    n2 = float(input("Getal 2: "))
    totaal = addition(n1, n2)
    print (f"{n1} + {n2} = {totaal}")
# ------------------------------------------------------- 
elif choice.lower() == "b":
    n1= float(input("Getal 1: "))
    n2 = float(input("Getal 2: "))
    totaal = subtraction(n1, n2)
    print (f"{n1} - {n2} = {totaal}")
# ------------------------------------------------------- 
elif choice.lower() == "c":
    n1= float(input("Getal 1: "))
    n2 = float(input("Getal 2: "))
    totaal = multiplication(n1, n2)
    print (f"{n1} x {n2} = {totaal}")
# ------------------------------------------------------- 
elif choice.lower() == "d":
    n1= float(input("Getal 1: "))
    n2 = float(input("Getal 2: "))
    totaal = division(n1, n2)
    print (f"{n1} : {n2} = {totaal}")
# ------------------------------------------------------- 
elif choice.lower() == "e":
    n1= float(input("Getal?: "))
    n2= 1
    totaal = addition(n1, n2)
    print (f"{n1} + {n2} = {totaal}")
# ------------------------------------------------------- 
elif choice.lower() == "f":
    n1= float(input("Getal?: "))
    n2= 1
    totaal = subtraction(n1, n2)
    print (f"{n1} - {n2} = {totaal}")
# ------------------------------------------------------- 
elif choice.lower() == "g":
    n1= float(input("Getal?: "))
    n2= 2
    totaal = multiplication(n1, n2)
    print (f"{n1} x {n2} = {totaal}")
# ------------------------------------------------------- 
elif choice.lower() == "h":
    n1= float(input("Getal?: "))
    n2 = 2
    totaal = division(n1, n2)
    print (f"{n1} : {n2} = {totaal}")
# -------------------------------------------------------
print("Wat wilt u doen met het vorige getal?","("+str(totaal)+")")