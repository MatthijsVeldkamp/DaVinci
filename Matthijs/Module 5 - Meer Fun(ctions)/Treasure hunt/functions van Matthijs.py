import time
import math
from termcolor import colored
from data import JOURNEY_IN_DAYS
from data import COST_FOOD_HORSE_COPPER_PER_DAY
from data import COST_FOOD_HUMAN_COPPER_PER_DAY
from data import COST_TENT_GOLD_PER_WEEK
from data import COST_HORSE_SILVER_PER_DAY
##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    return round(amount/10,2)

def silver2gold(amount:int) -> float:
    return round(amount/5,2)

def copper2gold(amount:int) -> float:
    num = copper2silver(amount)
    return silver2gold(num)

def platinum2gold(amount:int) -> float:
    return round(amount*25,2)

# def getPersonCashInGold(personCash:dict) -> float:
#     gold1 = platinum2gold(personCash['platinum'])
#     gold2 = silver2gold(personCash['silver'])
#     gold3 = copper2gold(personCash['copper'])
#     golderbij = gold1 + gold2 + gold3
#     personCash = personCash['gold'] + golderbij
#     return round(personCash,2)
def getPersonCashInGold(personCash:dict) -> float:
    num1 = copper2gold(personCash['copper'])
    num2 = silver2gold(personCash['silver'])
    num3 = platinum2gold(personCash['platinum'])
    num4 = personCash['gold']
    geheel = round(num1+num2+num3+num4,2)
    return geheel
##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    peopleamountCopper = people * COST_FOOD_HUMAN_COPPER_PER_DAY
    peopleamountCopper = peopleamountCopper * JOURNEY_IN_DAYS
    peopleamountGold = copper2gold(peopleamountCopper)
    round(peopleamountGold,2)
    horseamountcopper = horses * COST_FOOD_HORSE_COPPER_PER_DAY
    horseamountcopper = horseamountcopper * JOURNEY_IN_DAYS
    horseamountgold = copper2gold(horseamountcopper)
    round(horseamountgold,2)
    totaalperdag = horseamountgold + peopleamountGold
    return round(totaalperdag,2)
##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    return[item for item in list if item[key] == value]
def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs (people,"adventuring",True)

def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs (friends,"shareWith",True)

def getAdventuringFriends(friends:list) -> list:
    namenlijst = []
    for i in range (len(friends)):
        if friends[i]['adventuring'] and friends[i]['shareWith'] == True:
            namenlijst.append(friends[i])
    return (namenlijst)

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people/2)

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people/3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    return (horses * silver2gold(COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS) + (tents * (COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS / 7)) )
##################### M04.D02.O7 #####################

# def getItemsAsText(items:list) -> str:
#     nieuwelijst = []
#     for i in range(len(items)):
#         nieuwelijst.append(str(items[i]["amount"]) + str(items[i]["unit"]) + " " + str(items[i]["name"]))
#     nieuwelijst = str(nieuwelijst)
#     nieuwelijst = nieuwelijst.replace("[","")
#     nieuwelijst = nieuwelijst.replace("]","")
#     nieuwelijst = nieuwelijst.replace("'","")
#     return nieuwelijst
def getItemsAsText(items:list) -> str:
    namenitems = []
    for i in range(len(items)):
        naam= items[i]['name']
        aantal =items[i]['amount']
        unit =items[i]['unit']
        itemsastext=aantal,unit,naam
        namenitems.append(itemsastext)
    return namenitems

def getItemsValueInGold(items:list) -> float:
    prijsproduct=0
    for i in items:
        type=i['price']['type']
        prijs=i['price']['amount']
        aantal=i['amount']
        if type=='copper':
            prijstotaal=copper2gold(prijs)*aantal
        elif type=='silver':
            prijstotaal=silver2gold(prijs)*aantal
        elif type=='platinum':
            prijstotaal=platinum2gold(prijs)*aantal
        elif type=='gold':
            prijstotaal=prijs*aantal
        prijsproduct+=prijstotaal
    return prijsproduct

##################### M04.D02.O8 #####################

# def getCashInGoldFromPeople(people:list) -> float:
#     goldtotal = 0
#     for person in people:
#         print(person["cash"])
#         golderbij = getPersonCashInGold(person["cash"]) #  >:(
#         goldtotal += golderbij
#     return round(goldtotal,2)
def getCashInGoldFromPeople(people:list) -> float:
    copperingold=0
    silveringold=0
    goldingold=0
    platinumingold=0
    for money in people:
        copper=money['cash']['copper'] #:(
        silver=money['cash']['silver']
        gold=money['cash']['gold']
        platinum=money['cash']['platinum']
        copperingold+=copper2gold(copper)
        silveringold+=silver2gold(silver)
        goldingold+=gold
        platinumingold+=platinum2gold(platinum)
    goldingold+=copperingold+silveringold+platinumingold 
    return round(goldingold,2)

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    InterestingInvestors = []
    for i in range(len(investors)):
        if (investors[i]["profitReturn"]) <= 10:
            InterestingInvestors.append(investors[i]["name"])
    return(InterestingInvestors)
    

def getAdventuringInvestors(investors:list) -> list:
    AdventuringInvestors = []
    for i in range(len(investors)):
        profitreturn = investors[i]["profitReturn"]
        if profitreturn <= 10 and (investors[i]["adventuring"] == True):
            AdventuringInvestors.append(investors[i])
    return(AdventuringInvestors)
    

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    hoeveelmee = len(getAdventuringInvestors(investors))
    kostenvoortent = COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS / 7)
    kostenvoorpaard = silver2gold(COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS * hoeveelmee
    horsesCost = copper2gold(hoeveelmee * COST_FOOD_HORSE_COPPER_PER_DAY * JOURNEY_IN_DAYS)
    investorCostfood = copper2gold(COST_FOOD_HUMAN_COPPER_PER_DAY * JOURNEY_IN_DAYS * hoeveelmee)
    costgear = getItemsValueInGold(gear)
    return round(kostenvoortent + kostenvoorpaard + investorCostfood + costgear + horsesCost,2)
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