friends = [{
    'name' : 'Jorick',
    'shareWith' : True,
    'adventuring' : True,
    'cash' : {
        'platinum' : 0,
        'gold' : 9,
        'silver' : 9,
        'copper' : 43
    }
}]
adventurerGear = [{
    'name' : 'Lantaren',
    'amount' : 1,
    'unit' : 'x',
    'price' : {
        'amount' : 2,
        'type' : 'gold'
    }
}]
def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount:int) -> float:
    return amount / 50

def platinum2gold(amount:int) -> float:
    return amount * 25
# print(friends[0]["name"])
if (adventurerGear[0]["price"]["type"]) == "gold":
    print(adventurerGear[0]["name"],"staat al in gold!")
    print("Het kost",adventurerGear[0]["price"]["amount"],"gold!")
elif (adventurerGear[0]["price"]["type"]) == "silver":
    print(adventurerGear[0]["name"],"staat in silver!")
    togold = silver2gold(adventurerGear[0]["price"]["amount"])
    round(togold, 2)
    print("In gold is dit:",togold)
elif (adventurerGear[0]["price"]["type"]) == "copper":
    print(adventurerGear[0]["name"],"staat in copper!")
    togold = copper2gold(adventurerGear[0]["price"]["amount"])
    round(togold, 2)
    print("In gold is dit:",togold)