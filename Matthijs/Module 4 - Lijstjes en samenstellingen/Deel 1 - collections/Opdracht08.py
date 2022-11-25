from fruitmand import *
watermeloen = {
    "name" : "watermeloen",
    "weight" : 2500,
    "color" : "groen",
    "round" : True
}
fruitmand.append(watermeloen)
for i in range(len(fruitmand)):
    print(fruitmand[i]["weight"])