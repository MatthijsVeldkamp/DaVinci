from fruitmand import *
lijst = {}
for i in range(len(fruitmand)):
    lijst.update({fruitmand[i].get("weight"): fruitmand[i].get("name")})
for i in (fruitmand):
    lijst.update({i.get("weight"): i.get("name")})
print(sorted(lijst.items(), reverse=True))