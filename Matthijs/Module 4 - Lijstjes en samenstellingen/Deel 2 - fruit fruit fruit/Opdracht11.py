from fruitmand import *
loop = True
kleuren = []
naam = []
lijstkleuren = []
rond = 0
nietrond = 0
for x in range(len(fruitmand)):
    kleur = (fruitmand[x]['color'])
    if kleur not in lijstkleuren:
        lijstkleuren.append(kleur)
while loop == True:
    kleur = str(input("Kies een kleur uit de kleuren" + str(lijstkleuren)+"\n? "))
    if (kleur.lower()) not in lijstkleuren:
        print ("De Kleur " + kleur + " zit er niet in de fruitmand")
        loop = True
    else:
        print("Kleur zit in de lijst.")
        loop = False
for fruit in fruitmand:
            if fruit['color'] == kleur:
                if fruit['round'] == True:
                    rond += 1
                else:
                    nietrond += 1
print (rond)
print (nietrond)
verschil = rond - nietrond
verschil = abs(verschil)
if rond > nietrond:
    print (f"Er zijn {int(verschil)} meer ronde vruchten dan niet ronde vruchten in de kleur {str(kleur)}")
if rond < nietrond:
        print (f"Er zijn {str(verschil)} minder ronde vruchten dan niet ronde vruchten in de kleur {str(kleur)}")
if rond == nietrond:
    print (f"Er zijn {str(verschil)} ronde vruchten en {str(nietrond)} niet ronde vruchten in de kleur {str(kleur)}")