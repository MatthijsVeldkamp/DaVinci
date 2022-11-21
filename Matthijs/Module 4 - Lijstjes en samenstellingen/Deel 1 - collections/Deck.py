import random
speciaal = ("harten","ruiten","klaveren","schoppen")
kaarten = ("2","3","4","5","6","7","8","9","10","boer","vrouw","heer","aas")
deck = []
nummer = 0
nummer1 = 1
nummer2 = 0
for i in range(4):
    for i in range (13):
        deck.append(speciaal[nummer]+ " " + kaarten[i])
    nummer += 1
for i in range(2):
    deck.append("joker")
random.shuffle(deck)
for i in range(7):
    print("Kaart "+ str(nummer1)+": "+deck[nummer2])
    nummer1 += 1
    nummer2 += 1
print(deck)