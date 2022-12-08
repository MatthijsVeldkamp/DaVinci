while True:
    try:
        hoeveel = int(input("Hoeveel keer? "))
        break
    except:
        print("vul alleen nummers in!")
        continue
def hello(hoeveel:int) -> str:
    result = ""
    for i in range(hoeveel):
        result += f"Hello from function town! {i+1}\n"
    return result
print(hello(hoeveel))