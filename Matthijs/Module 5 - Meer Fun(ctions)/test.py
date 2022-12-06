x = True
def plus(getal1:int, getal2:int) -> int:
    return getal1 + getal2
def min(getal1:int, getal2:int) -> int:
    return getal1 - getal2
def keer(getal1:int, getal2:int) -> float:
    return getal1 * getal2
def delen(getal1:int, getal2:int) -> float:
    try:
        return getal1 / getal2
    except:
        print("Kan niet delen door 0!")
        x = False
# print(plus(1,2))
a = int(input("Getal 1: "))
b = int(input("Getal 2: "))
if x == True:
    print("Dat is:",(delen(a,b)))
else:
    pass