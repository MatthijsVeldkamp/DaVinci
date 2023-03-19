aantalbolletjes = 0
welkesmaken = ["chocola", "aardbei", "munt", "mokka", "walnoot","vanille"]
smaken = []
def vraag():
    try:
        aantalbolletjes = int(input("Hoeveel bolletjes ijs wilt u? "))
        return aantalbolletjes
    except:
        print("Sorry, dat snap ik niet.")
        vraag()
aantalbolletjes = vraag()
for aantalbolletjes in range(aantalbolletjes):
    while True:
        smaak = input(f"Welke smaak wilt u voor bolletje {aantalbolletjes+1}? ").lower()
        # checken of de smaak in de lijst welkesmaken staat
        if smaak in welkesmaken:
            smaken.append(smaak)
            break
        else:
            print("Sorry, die hebben we niet.")
            aantalbolletjes - 1
            continue
for aantalbolletjes in range(aantalbolletjes+1):
    print(f"bolletje {aantalbolletjes+1}: {smaken[aantalbolletjes]}")