import random
namen = ["Matthijs","Luc","Kjeld"]
koppel1 = []
koppel2 = []
while True:
    koppel1.append(random.choice(namen))
    koppel2.append(random.choice(namen))
    if koppel1 == koppel2:
        koppel1 = []
        koppel2 = []
    else:
        break
print(str(koppel1) +" heeft "+ str(koppel2))