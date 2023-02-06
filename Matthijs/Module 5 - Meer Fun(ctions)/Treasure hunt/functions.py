import time
import math
from termcolor import colored
from data import *
##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount:int) -> float:
    return amount / 50

def platinum2gold(amount:int) -> float:
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    gold = personCash["gold"]
    gold += silver2gold(personCash["silver"])
    gold += copper2gold(personCash["copper"])
    gold += platinum2gold(personCash["platinum"])
    return gold
##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    peopleamountcopper = people * COST_FOOD_HUMAN_COPPER_PER_DAY
    peopleamountcopper = peopleamountcopper * JOURNEY_IN_DAYS
    peopleamountgold = copper2gold(peopleamountcopper)
    round(peopleamountgold,2)
    horseamountcopper = horses * COST_FOOD_HORSE_COPPER_PER_DAY
    horseamountcopper = horseamountcopper * JOURNEY_IN_DAYS
    horseamountgold = copper2gold(horseamountcopper)
    round(horseamountgold,2)
    totaalperdag = horseamountgold + peopleamountgold
    return round(totaalperdag,2)
##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    return [item for item in list if item[key] == value]
def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs (people,"adventuring",True)

def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs (friends,"sharewith",True)

def getAdventuringFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, "adventuring", True)

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people/2)

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people/3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    return (horses * silver2gold(COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS) + (tents * (COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS / 7)) )
##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    nieuwelijst = []
    for i in range(len(items)):
        nieuwelijst.append(str(items[i]["amount"]) + str(items[i]["unit"]) + " " + str(items[i]["name"]))
    nieuwelijst = str(nieuwelijst)
    nieuwelijst = nieuwelijst.replace("[","")
    nieuwelijst = nieuwelijst.replace("]","")
    nieuwelijst = nieuwelijst.replace("'","")
    return nieuwelijst

def getItemsValueInGold(items:list) -> float:
    totaalaantalgoud = 0
    for i in range (len(items)):
        typengeld = (items[i]['price']['type'])
        if typengeld == 'copper':
            totaalaantalgoud += copper2gold(items[i]['amount'] * items[i]['price']['amount'])
        elif typengeld == 'platinum':
            totaalaantalgoud += platinum2gold(items[i]['amount'] * items[i]['price']['amount'])
        elif typengeld == 'silver':
            totaalaantalgoud += silver2gold(items[i]['amount'] * items[i]['price']['amount'])
        elif typengeld == 'gold':
            totaalaantalgoud += (items[i]['amount'] * items[i]['price']['amount'])
    return round(totaalaantalgoud,2)

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:list) -> float:
    pass

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()
