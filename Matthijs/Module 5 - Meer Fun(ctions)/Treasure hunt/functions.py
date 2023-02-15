import time
import math
from termcolor import colored
#from data import JOURNEY_IN_DAYS
#from data import COST_FOOD_HUMAN_COPPER_PER_DAY 
#from data import COST_FOOD_HORSE_COPPER_PER_DAY
#from data import COST_TENT_GOLD_PER_WEEK
#from data import COST_HORSE_SILVER_PER_DAY
from data import *

##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    return round(amount / 10, 2)

def silver2gold(amount:int) -> float:
    return round(amount / 5, 2)

def copper2gold(amount:int) -> float:
    result = copper2silver(amount)
    return silver2gold(result)

def platinum2gold(amount:int) -> float:
    return round(amount * 25, 2)

def getPersonCashInGold(personCash:dict) -> float:
    gold = platinum2gold(personCash["platinum"])
    gold += personCash["gold"]
    gold += silver2gold(personCash["silver"])
    gold += copper2gold(personCash["copper"])
    return round(gold, 2)

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    foodCostPeople = JOURNEY_IN_DAYS * COST_FOOD_HUMAN_COPPER_PER_DAY * people
    foodCostHorses = JOURNEY_IN_DAYS * COST_FOOD_HORSE_COPPER_PER_DAY * horses
    return copper2gold(foodCostPeople + foodCostHorses)

##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    friends = []
    for friend in list:
        if friend[key] == value:
            friends.append(friend)
    return friends


def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, "adventuring", True)


def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, "shareWith", True)

def getAdventuringFriends(friends:list) -> list:
    return getAdventuringPeople(getShareWithFriends(friends))

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    costHorses = JOURNEY_IN_DAYS * horses * silver2gold(COST_HORSE_SILVER_PER_DAY)
    costTents = math.ceil(JOURNEY_IN_DAYS / 7) * tents * COST_TENT_GOLD_PER_WEEK    
    return round(costHorses + costTents, 2)



##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    text = ""
    space = ""
    for item in items:
        text += f"{space}{item['amount']}{item['unit']} {item['name']}"
        space = ", "

    return text

def getItemsValueInGold(items:list) -> float:
    totalPriceInGold = 0

    for item in items:
        priceInGold = item['price']['amount']
        if item['price']['type'] == 'silver':
            priceInGold = silver2gold(priceInGold)
        elif item['price']['type'] == 'copper':
            priceInGold = copper2gold(priceInGold)
        elif item['price']['type'] == 'platinum':
            priceInGold = platinum2gold(priceInGold)

        totalPriceInGold += priceInGold * item['amount']

    return round(totalPriceInGold,2)

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    cash = 0
    
    for person in people:
        cash += getPersonCashInGold(person['cash'])

    return round(cash,2)

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    interestingInvestors = []

    for investor in investors:
        if investor["profitReturn"] < 10: # maximaal 9% profitReturn
            interestingInvestors.append(investor)
    
    return interestingInvestors


def getAdventuringInvestors(investors:list) -> list:
    return getFromListByKeyIs(getInterestingInvestors(investors), "adventuring", True)


def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    adventuringInvestors = getAdventuringInvestors(investors)
    countInvestors = len(adventuringInvestors)
    
    # kosten voor paarden en tenten
    rentalCost = getTotalRentalCost(countInvestors, countInvestors)

    # kosten voor uitrusting
    gearCost = getItemsValueInGold(gear)

    # kosten voor eten
    foodCost = getJourneyFoodCostsInGold(countInvestors, countInvestors)

    return round(rentalCost + gearCost + foodCost,2)

    


##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    people_per_night_gold = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    horses_per_night_gold = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    return int(leftoverGold / (people_per_night_gold + horses_per_night_gold))

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    gold_per_night = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT)
    horses_gold_per_night = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT)
    human_per_night_Gold =  gold_per_night * people 
    horses_per_night_Gold = horses_gold_per_night * horses 
    return round((human_per_night_Gold + horses_per_night_Gold) * nightsInInn,2)

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    investorlist = []
    for a in investors:
        if a['profitReturn'] < 10:
            investorlist.append(round(a['profitReturn'] / 100 * profitGold,2) )
    return investorlist
def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:list) -> float:
    investor_cuts = 0
    for a in investorsCuts:
        investor_cuts += a
    return round((profitGold - investor_cuts) / fellowship,2)
##################### M04.D02.O13 #####################
def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []
    # haal de juiste inhoud op
    adventuringFriends = [friends]
    interestingInvestors = [investors]
    adventuringInvestors = [getInterestingInvestors(investors)]
    investorsCuts = []
    goldCut = 0.0
    # verdeel de uitkomsten
    for person in people:
        #code aanvullen
        earnings.append({
            'name'   : adventuringFriends[0],
            'start'  : 0.0,
            'end'    : 0.0
        })
    return earnings
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