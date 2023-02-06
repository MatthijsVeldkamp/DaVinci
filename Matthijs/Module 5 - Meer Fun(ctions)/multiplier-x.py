def multiply(getal:int) -> int:
    for i in range(10):
        print(f"{i+1} X {getal} = {getal * i+getal}")
try:
    getal = int(input("Welke tafel wilt u zien? "))
except:
    print("Vul allen nummers in!")
multiply(getal)