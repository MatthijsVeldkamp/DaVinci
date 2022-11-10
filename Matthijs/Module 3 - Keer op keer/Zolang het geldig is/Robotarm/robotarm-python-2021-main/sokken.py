import random 
wasmand = []
kleuren = ['wit', 'zwart', 'rood']
paren = 5
for kleur in kleuren:
    for x in range(paren*2):
        wasmand.append(kleur)
random.shuffle(wasmand)
hand = []
pickup = wasmand.pop(0)
while pickup not in hand:
    hand.append(pickup)
    pickup = wasmand.pop(0)
else:
    hand.append(pickup)
print(hand)