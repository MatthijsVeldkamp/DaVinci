import time
import math
from data import (COST_FOOD_HORSE_COPPER_PER_DAY,COST_FOOD_HUMAN_COPPER_PER_DAY,JOURNEY_IN_DAYS,COST_HORSE_SILVER_PER_DAY,COST_TENT_GOLD_PER_WEEK,COST_INN_HORSE_COPPER_PER_NIGHT,COST_INN_HUMAN_SILVER_PER_NIGHT)
from termcolor import colored

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

def getPersonCashInGold(personCash:dict) -> float:
    num1 = copper2gold(personCash['copper'])
    num2 = silver2gold(personCash['silver'])
    num3 = platinum2gold(personCash['platinum'])
    num4 = personCash['gold']
    geheel = round(num1+num2+num3+num4,2)
    return geheel
    

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    kostenDag = horses * COST_FOOD_HORSE_COPPER_PER_DAY + people * COST_FOOD_HUMAN_COPPER_PER_DAY
    kostenTotaal = JOURNEY_IN_DAYS * kostenDag
    koper = copper2gold(kostenTotaal)
    return koper

##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    personlist= []
    for i in list:
        if i[key] == value:
            personlist.append(i)
    return personlist

def getAdventuringPeople(people:list) -> list:
    var1 =getFromListByKeyIs(people,'adventuring', True)
    return var1

def getShareWithFriends(friends:list) -> int:
    var1 = getFromListByKeyIs(friends,'shareWith', True)
    return var1

def getAdventuringFriends(friends:list) -> list:
    var1=getAdventuringPeople(friends)
    var2=getShareWithFriends(var1)
    return var2
    
##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    numberofhorsesneeded=people/2
    return math.ceil(numberofhorsesneeded)

def getNumberOfTentsNeeded(people:int) -> int:
    numberoftentsneeded=people/3
    math.ceil(numberoftentsneeded)
    return math.ceil(numberoftentsneeded)

def getTotalRentalCost(horses:int, tents:int) -> float:
    costhorses=horses*COST_HORSE_SILVER_PER_DAY*JOURNEY_IN_DAYS
    costhorsesingold=silver2gold(costhorses)
    costtents=tents*COST_TENT_GOLD_PER_WEEK*2
    totalcost=costhorsesingold+costtents
    return totalcost

##################### M04.D02.O7 #####################

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

def getCashInGoldFromPeople(people:list) -> float:
    copperingold=0
    silveringold=0
    goldingold=0
    platinumingold=0
    for money in people:
        copper=money['cash']['copper']
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
    investorslagerdan10procent = []
    for i in investors:
        if i['profitReturn'] < 10:
            investorslagerdan10procent.append(i)
    return investorslagerdan10procent
def getAdventuringInvestors(investors:list) -> list:
    investorslagerdantienprocent=getInterestingInvestors(investors)
    investorsdiemeegaan = []
    for i in investorslagerdantienprocent:
        if i['adventuring']==True:
            investorsdiemeegaan.append(i)
    return investorsdiemeegaan

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    totaalbedrag=0
    aantalinvestors=len(getAdventuringInvestors(investors))
    prijsgear=getItemsValueInGold(gear)*aantalinvestors
    bedragtentg=aantalinvestors*COST_TENT_GOLD_PER_WEEK*2
    bedragetenc=aantalinvestors*COST_FOOD_HUMAN_COPPER_PER_DAY*JOURNEY_IN_DAYS
    bedragetenpaardc=aantalinvestors*COST_FOOD_HORSE_COPPER_PER_DAY*JOURNEY_IN_DAYS
    bedragpaards=aantalinvestors*COST_HORSE_SILVER_PER_DAY*JOURNEY_IN_DAYS
    bedrageteningold=copper2gold(bedragetenc)
    bedragetenpaardingold=copper2gold(bedragetenpaardc)
    bedragpaardingold=silver2gold(bedragpaards)
    totaalbedrag+=bedragtentg+bedrageteningold+bedragetenpaardingold+bedragpaardingold+prijsgear
    return round(totaalbedrag,2)
    

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    costhorses=copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT*horses)
    costpeople=silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT*people)
    cost1night=costhorses+costpeople
    amountofdays=leftoverGold/cost1night
    return math.floor(amountofdays)

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    peopleCost = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT * people) * nightsInInn
    horsesCost = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT * horses) * nightsInInn
    return round(peopleCost + horsesCost, 2)

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    totalprofitcut=[]
    investorslagerdan10procent = []
    for i in investors:
        if i['profitReturn'] < 10:
            investorslagerdan10procent.append(i)
    for i in investorslagerdan10procent:
        percentage=i['profitReturn']
        profitcut=profitGold/100*percentage
        totalprofitcut.append(profitcut)
    return totalprofitcut

def getAdventurerCut(profitGold:float, investorsCuts:list, poeple:int) -> float:
    goldToDevide = round(profitGold, 2)
    return round(goldToDevide / poeple, 2)

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    
    earnings = []
    # haal de juiste inhoud op
    interestingInvestors = getInterestingInvestors(investors)
    investorsCuts = getInvestorsCuts(profitGold,investors)
    goldCut = getAdventurerCut(profitGold,investorsCuts,6)
    people = [mainCharacter] + friends + interestingInvestors
    investorscutsnames= [{
    'name' : 'Cipher',
    'cut' : 56.676,
    }
,{
    'name' : 'Dwindel',
    'cut' : 85.014,
    }
]

    for person in people:
        name=person['name']
        if person in investors:
            geldstart=getPersonCashInGold(person['cash'])
            for i in investorscutsnames:
                if i['name']==person['name']:
                    investorcut=i['cut']
                    geldeind=geldstart+investorcut

                
        else:
            if person['name'] != 'Goudklomp':
                geldstart=getPersonCashInGold(person['cash'])
                geldeind=geldstart+goldCut-10
            else:
                geldstart=getPersonCashInGold(person['cash'])
                geldeind=geldstart+goldCut+10*5

        earnings.append({
        'name': name,
        'start': geldstart,
        'end': geldeind
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