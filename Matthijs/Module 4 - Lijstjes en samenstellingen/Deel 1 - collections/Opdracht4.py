from fruitmand import *
import random
y = True
x = len(fruitmand)
while y == True:
    try:
        aantal = int(input("Hoeveel? "))
    except:
        print("Vul alleen nummers in!")
        continue
    for i in range(aantal):
        randomgetal = random.randint(1,x)
        print(fruitmand[randomgetal]['name'])
        y = False