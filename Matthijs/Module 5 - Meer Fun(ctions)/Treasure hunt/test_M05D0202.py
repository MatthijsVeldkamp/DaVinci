from functions import print_colorvars
from functions import copper2silver, silver2gold, copper2gold, platinum2gold, getPersonCashInGold

if copper2silver(10) != 1.0:
    print_colorvars(vars=['Test 1 is False'], color='red')
else:
    print_colorvars(vars=['Test 1 is correct'], color='green')

if copper2silver(11) != 1.1:
    print_colorvars(vars=['Test 2 is False'], color='red')
else:
    print_colorvars(vars=['Test 2 is correct'], color='green')

if silver2gold(10) != 2.0:
    print_colorvars(vars=['Test 3 is False'], color='red')
else:
    print_colorvars(vars=['Test 3 is correct'], color='green')

if silver2gold(13) != 2.6:
    print_colorvars(vars=['Test 4 is False'], color='red')
else:
    print_colorvars(vars=['Test 4 is correct'], color='green')

if copper2gold(10) != 0.2:
    print_colorvars(vars=['Test 5 is False'], color='red')
else:
    print_colorvars(vars=['Test 5 is correct'], color='green')

if copper2gold(16) != 0.32:
    print_colorvars(vars=['Test 6 is False'], color='red')
else:
    print_colorvars(vars=['Test 6 is correct'], color='green')

if platinum2gold(1) != 25:
    print_colorvars(vars=['Test 7 is False'], color='red')
else:
    print_colorvars(vars=['Test 7 is correct'], color='green')

if platinum2gold(10) != 250:
    print_colorvars(vars=['Test 8 is False'], color='red')
else:
    print_colorvars(vars=['Test 8 is correct'], color='green')

lestDictionairy1 = {
    'platinum' : 1,
    'gold' : 1,
    'silver' : 1,
    'copper' : 1
}

if getPersonCashInGold(lestDictionairy1) != 26.22:
    print_colorvars(vars=['Test 9 is False'], color='red')
else:
    print_colorvars(vars=['Test 9 is correct'], color='green')

lestDictionairy2 = {
    'platinum' : 22,
    'gold' : 38,
    'silver' : 12,
    'copper' : 3120
}

if getPersonCashInGold(lestDictionairy2) != 652.8:
    print_colorvars(vars=['Test 10 is False'], color='red')
else:
    print_colorvars(vars=['Test 10 is correct'], color='green')
