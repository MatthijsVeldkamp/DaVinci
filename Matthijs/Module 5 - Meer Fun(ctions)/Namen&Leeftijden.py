def naam_en_leeftijd() -> list:
    lijst = []
    loop = True
    while loop == True:
        naam = input("Naam? ")
        if naam == "stop":
            break
        leeftijd = input("Leeftijd? ")
        if leeftijd == "stop":
            break
        bijelkaar = {'naam': naam, 'leeftijd' : leeftijd,}
        lijst.append(bijelkaar)
    return(lijst)
for person in naam_en_leeftijd():
    print(f"{person['naam']} is {person['leeftijd']} jaar")