from fruitmand import *
namen = []
tellen = []
voorindex = 0
vertaling = {
    "red" : "rode",
    "orange" : "oranje",
    "green" : "groene",
    "brown" : "bruine",
    "yellow" : "gele"
}
for x in range(len(fruitmand)):
    namen.append(fruitmand[x]["name"])
namen.sort(key=len)
namen.reverse()
langste = namen[0]
letters = len(langste)
for x in range(len(fruitmand)):
    if fruitmand[x]["name"]== langste:
        gewicht = fruitmand[x]["weight"]
        kleur = fruitmand[x]["color"]
gewicht = gewicht / 1000



print("De",langste,"(",letters,"letters ) heeft een",vertaling[kleur],"kleur en een gewicht van",gewicht,"Kg." )