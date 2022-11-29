from fruitmand import *
totaalgewicht = []
gewicht = 0
kg = str(" kg")
watermeloen = {
    "name" : "watermeloen",
    "weight" : 2500,
    "color" : "green",
    "round" : True
}
fruitmand.append(watermeloen)
for i in range(len(fruitmand)):
    totaalgewicht.append(fruitmand[i]["weight"])
for x in range(len(totaalgewicht)):
    gewicht = gewicht + int(totaalgewicht[x])
gewicht = gewicht / 1000
print(gewicht," kg")