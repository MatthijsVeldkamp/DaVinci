import random
kleuren = ["rood","blauw","groen","geel","bruin","roze"]
hoeveelheid = input("Hoeveel M&M's wilt u?\n? ")
randomlijst = []
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

for i in range(int(hoeveelheid)):
    randomlijst.append(random.choice(kleuren))
a = randomlijst.count("rood")
b = randomlijst.count("blauw")
c = randomlijst.count("groen")
d = randomlijst.count("geel")
e = randomlijst.count("bruin")
f = randomlijst.count("roze")
zak = {
    "Rood" : a,
    "Blauw" : b,
    "Groen" : c,
    "Geel" : d,
    "Bruin" : e,
    "Roze" : f
}
print(zak)