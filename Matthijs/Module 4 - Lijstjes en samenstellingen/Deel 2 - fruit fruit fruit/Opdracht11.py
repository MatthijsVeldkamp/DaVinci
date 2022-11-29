from fruitmand import *
loop = True
kleuren = []
lijstkleuren = []
for x in range(len(fruitmand)):
    kleur = (fruitmand[x]['color'])
    if kleur not in lijstkleuren:
        lijstkleuren.append(kleur)

while loop == True:
    kleur = str(input("Kies een kleur uit de kleuren" + str(lijstkleuren)))
    if (kleur.lower()) not in lijstkleuren:
        print ("De Kleur " + kleur + " zit er niet in de fruitmand")
        loop = True
    else:
        print("Kleur zit in de lijst.")
        loop = False

    for x in range(len(fruitmand)):
        kleuren.append(fruitmand[x]["round"])
    rond = kleuren.count(True)
    nietrond= kleuren.count(False)
    som = (rond-nietrond)
    if som <0:
        som = abs(som)
        print("er is",som, "meer niet ronde dan ronde van de kleur",kleur)
        break
    elif som >0:
        print("er is",som, "meer ronde dan niet ronde")
        break
    elif som == 0:
        print("er zijn evenveel ronde als niet ronde")
        break