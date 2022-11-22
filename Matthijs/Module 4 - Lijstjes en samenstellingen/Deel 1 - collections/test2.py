boodschappenlijstje = {
    
}
input1 = input("add to dictionary? ")
input1.lower()
boodschappenlijstje[input1] = 1
boodschappenlijstje =  {k.lower(): v for k, v in boodschappenlijstje.items()}
print(boodschappenlijstje)