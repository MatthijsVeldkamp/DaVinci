def multiply(getal:int) -> int:
    for i in range(10):
        print(i+1,"X",getal,"=",getal * i+getal)
getal = int(input("Welke tafel wilt u zien? "))
multiply(getal)