lijst = []
def naam_en_leeftijd():
    loop = True
    while loop == True:
        naam = input("Naam? ")
        if naam == "stop":
            return
        leeftijd = input("Leeftijd? ")
        if leeftijd == "stop":
            return
        bijelkaar = {'naam': naam, 'leeftijd' : leeftijd,}
        lijst.append(bijelkaar)
naam_en_leeftijd()
for i in range (len(lijst)):
    print(f"{lijst[i]['naam']} is {lijst[i]['leeftijd']} jaar oud.")