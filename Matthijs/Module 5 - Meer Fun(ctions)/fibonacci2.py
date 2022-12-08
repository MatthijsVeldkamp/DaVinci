# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946
import sys
sys.setrecursionlimit(15000)
getallen = [0]
def factorial(x:int,hoeveel:int,a:int,b:int,som:int):
    if x == (hoeveel):
        pass
    else:
        x += 1
        volgende = getallen.append(getallen[a]+getallen[b])
        a += 1
        b += 1
        factorial(x,hoeveel,a,b,som)
        return (getallen)
hoeveel = int(input("Hoeveel? "))
a = 0
b = 1
som = a+b
getallen.append(som)
factorial(0,hoeveel,a,b,som)
print(getallen)