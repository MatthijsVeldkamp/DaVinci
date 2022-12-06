hoeveel = int(input("Hoeveel keer? "))
def hello(hoeveel:int) -> str:
    for i in range(hoeveel):
        print("Hello from function town! "+str(i+1))
hello(hoeveel)