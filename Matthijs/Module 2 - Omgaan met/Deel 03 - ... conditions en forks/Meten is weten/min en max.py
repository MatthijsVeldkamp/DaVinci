a = float(input("Getal 1: "))
b = float(input("Getal 2: "))
if a > b:
    max = (a)
    print("A is het grootste getal.")
    print(max)
    print("Het minimum is: ",b,)
    print("Het maximum is: ",a,)
elif b > a:
    min = (a)
    print("A is het kleinste getal.")
    print(min)
    print("Het minimum is: ",a,)
    print("Het maximum is: ",b,)
else:
    print("a en b zijn even groot.")