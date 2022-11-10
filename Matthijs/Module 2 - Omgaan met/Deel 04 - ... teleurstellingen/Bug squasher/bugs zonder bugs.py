import random

name = input("Wat is jouw naam? ")
print("Hallo", name)

favoriteSeason = input("Wat is jouw favorite seizoen "+name+"? A) Lente, B) Zomer, C) Herfst of D) Winter ")
answer = favoriteSeason.lower()

if answer == 'a':
    print("Ik hou ook van de lente!")
elif answer == 'b':
    print("De zomer is voor mij te warm.")
elif answer == 'c':
    print("Mooi he, al die blaadjes die dan van de boom vallen.")
elif answer == 'd':
    print("Is de winter niet erg koud?")
else:
    print("Die ken ik niet...")

favoriteColor = input('En wat is je favoriete kleur? ') 
trueOrFalse = random.randint(0,1)
if trueOrFalse == 0:
    print('Ik vind dat ook een mooie kleur!')
elif trueOrFalse == 1:
    print("TBH, ik hou niet zo van de kleur "+favoriteColor+"...")

num1 = random.randint(1,10)
num2 = random.randint(5,15)
try:
    num3 = num1+num2
    num4 = float(input("En weet jij wat "+str(num1)+"+"+str(num2)+" is? "))
    if num4 == num3:
        print("Dat is juist")
    elif num4 != num3:  
        print("Nee dat klopt niet "+name)
except:
    print("Dat is geen nummer!")

