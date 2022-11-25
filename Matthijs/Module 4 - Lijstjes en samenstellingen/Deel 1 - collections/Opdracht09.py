from fruitmand import * 
kleurlijst = []
fruitmand.remove({'name' : 'druif', 'weight' : 5, 'color' : 'red', 'round' : True})
for i in range (len(fruitmand)):
    kleur = (fruitmand[i]['color'])
    if kleur not in kleurlijst:
        kleurlijst.append(kleur)
print (kleurlijst)