import random
spelerskaart = "joker"
beginkaart = "joker"
print(beginkaart)
print(spelerskaart)
if (spelerskaart.split(' ', 1)[0]) == (beginkaart.split(' ', 1)[0]):
    print("Actie toegelaten!")
elif (spelerskaart.split(' ', 1)[1]) == (beginkaart.split(' ', 1)[1]):
    print("Actie toegelaten!")
else:
    print("Actie niet toegelaten!")