import time
import os
items = []
clear = False
def clear_inventory():
    global clear
    clear = False
    items.clear()
def items_add(item):
    items.append(item)
def items_remove(item):
    items.remove(item)
def end_1():
    global einde
    print("\033[1;31;40m")
    print("Onjuiste code!")
    time.sleep(3)
    codegoed = 0
    os.system('cls')
    print("\033[1;31;40m")
    print("-----------------------------------------------")
    print("|                                             |")
    print("|                   Helaas...                 |")
    print("|    U kon niet uit het huis ontsnappen omdat |")
    print("|            u de code niet wist.             |")
    print("|                                             |")
    print("|                Einde 1 van 6                |")
    print("|                                             |")
    print("-----------------------------------------------")
    print("\033[1;37;40m")
    restart = input("Wilt u nog een keer?\nY/N? ")
    if restart.lower() == ("y"):
        einde = 0
    else:
        einde = 1
    if einde == 0:
        reset_variables()
        alles()
    print("\033[1;37;40m")
    return
def end_2():
    global einde
    os.system('cls')
    print("\033[1;31;40m")
    print("-----------------------------------------------")
    print("|                                             |")
    print("|                   Helaas...                 |")
    print("|          U viel van de trap af omdat        |")
    print("|                het te donker was            |")
    print("|                                             |")
    print("|                Einde 2 van 6                |")
    print("|                                             |")
    print("-----------------------------------------------")
    print("\033[1;37;40m")
    restart = input("Wilt u nog een keer?\nY/N? ")
    if restart.lower() == ("y"):
        einde = 0
    else:
        einde = 1
    if einde == 0:
        reset_variables()
        alles()
    print("\033[1;37;40m")
    return
def end_3():
    global einde
    os.system('cls')
    print("\033[1;31;40m")
    print("-----------------------------------------------")
    print("|                                             |")
    print("|                   Helaas...                 |")
    print("|          U heeft geen sleutel gevonden.     |")
    print("|       en kon hierdoor niet de deur openen   |")
    print("|                                             |")
    print("|                Einde 3 van 6                |")
    print("|                                             |")
    print("-----------------------------------------------")
    print("\033[1;37;40m")
    restart = input("Wilt u nog een keer?\nY/N? ")
    if restart.lower() == ("y"):
        einde = 0
    else:
        einde = 1
    if einde == 0:
        reset_variables()
        alles()
    print("\033[1;37;40m")
    return
def end_4():
    global einde
    global score
    os.system('cls')
    print("\033[1;32;40m")
    print("-----------------------------------------------")
    print("|                                             |")
    print("|                 Goed gedaan                 |")
    print("|         U ontsnaptte via de nooduitgang     |")
    print("|                                             |")
    print("|                Einde 4 van 6                |")
    print("|                                             |")
    print("-----------------------------------------------")
    restart = input("Wilt u nog een keer?\nY/N? ")
    if restart.lower() == ("y"):
        einde = 0
    else:
        einde = 1
    score += 1
    if einde == 0:
        reset_variables()
        alles()
    print("\033[1;37;40m")
    return
def end_5():
    global einde
    global score
    os.system('cls')
    print("\033[1;32;40m")
    print("-----------------------------------------------")
    print("|                                             |")
    print("|                 Goed gedaan                 |")
    print("|         U ontsnaptte via de nooduitgang     |")
    print("|                                             |")
    print("|                Einde 5 van 6                |")
    print("|                                             |")
    print("-----------------------------------------------")
    restart = input("Wilt u nog een keer?\nY/N? ")
    if restart.lower() == ("y"):
        einde = 0
    else:
        einde = 1
    score += 1
    if einde == 0:
        reset_variables()
        alles()
    print("\033[1;37;40m")
    return
def end_6():
    global einde
    os.system('cls')
    print("\033[1;31;40m")
    print("-----------------------------------------------")
    print("|                                             |")
    print("|                   Helaas...                 |")
    print("|          De batterijen van de zaklamp       |")
    print("|       zijn leeg en hierdoor kon u niet      |")
    print("|                 ontsnappen                  |")
    print("|                Einde 6 van 6                |")
    print("|                                             |")
    print("-----------------------------------------------")
    restart = input("Wilt u nog een keer?\nY/N? ")
    if restart.lower() == ("y"):
        einde = 0
    else:
        einde = 1
    if einde == 0:
        reset_variables()
        alles()
    print("\033[1;37;40m")
    return
# 37 = white, 33 = yellow, 34 = blue, 31 = red, 32 = green.
restart = ("ja")
score = 0
z = True
codegoed = 0
sleutel = False
kelder = False
einde = 0
item1 = str(" ")
item2 = str(" ")
boekgoed = False
rondkijken = False
batterijen = False
zaklamp = 0
def reset_variables():
    global z
    global codegoed
    global sleutel
    global kelder
    global einde
    global item1
    global item2
    global boekgoed
    global rondkijken
    global batterijen
    global zaklamp
    z = True
    codegoed = 0
    sleutel = False
    kelder = False
    einde = 0
    item1 = str(" ")
    item2 = str(" ")
    boekgoed = False
    rondkijken = False
    batterijen = False
    zaklamp = 0
class OptieError(Exception):
    pass
class MenuError(Exception):
    pass
class CodeError(Exception):
    pass
class Ending1(Exception):
    pass
class Ending2(Exception):
    pass
class Ending3(Exception):
    pass

def alles():
    global clear
    global z
    global codegoed
    global sleutel
    global kelder
    global einde
    global item1
    global item2
    global boekgoed
    global rondkijken
    global batterijen
    global zaklamp
    clear = True
    z = True
    codegoed = 0
    sleutel = False
    kelder = False
    einde = 0
    item1 = str(" ")
    item2 = str(" ")
    boekgoed = False
    rondkijken = False
    batterijen = False
    zaklamp = 0
    while True:
        if restart.lower() == ("nee"):
            break
        elif einde == 1:
            break
        else:
            print("\033[1;37;40m")
            os.system('cls')
            print("Score:",score)
            print("Start:\nStart het spel!\n")
            print("Instructies:\nEen korte uitleg van hoe het spel werkt.\n")
            try:
                print("Wat wilt u doen?")
                opties = input("? ")
                if opties.lower() == "instructies":
                    os.system('cls')
                    print("\033[1;37;40m")
                    print("U bevindt zich in de kelder van een groot oud huis, u moet weg zien te komen door de juiste opties te kiezen.")
                    time.sleep(3)
                    print("Wanneer u iets moet typen, staat er (Selecteer een optie:). Typ dan letterlijk de optie over die u wilt kiezen. (Hoofdletters maken niet uit en leestekens hoeft u niet te typen.)")
                    time.sleep(3)
                    print("Gebruik nooit nummers tenzij dat duidelijk gevraagd word.")
                    time.sleep(3)
                    print("Je kan ook altijd items typen om te kijken wat voor items je hebt.")
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print("Typ menu om terug te gaan naar het menu.")   
                    try:
                        menu = input("? ")
                        if menu.lower() == "menu":
                            continue
                        else:
                            raise MenuError
                    except OptieError:
                        print("\033[1;37;40m")
                        print("Dat was geen optie!")
                        print("Het programma start nu opnieuw!")
                        time.sleep(4)
                        continue
                        
                        
                
                elif opties.lower() == "start":
                    zaklamp = 0
                    fles = 0
                    os.system('cls')
                    print("\033[1;37;40m")
                    print("Type uw naam in.")
                    name = input("? ")
                
                
                    os.system('cls')
                    print("Welkom "+name+"")
                    time.sleep(0.5)
                
                
                    while z == True:
                        if codegoed == 0 and einde == 0:
                            os.system('cls')
                            print("\033[1;37;40m")
                            if clear == True:
                                clear_inventory()
                                reset_variables()
                            else:
                                pass
                            print("U bevindt zich in de kelder van een groot huis.")
                            if zaklamp == 0:
                                print("Het is helemaal donker.")
                            elif zaklamp == 1:
                                print("U gebruikt de zaklamp om te zien.")
                            time.sleep(0.5)
                            print("De enige opties zijn:\n")
                            if zaklamp == 1:
                                print("De trap omhoog.")
                            elif zaklamp == 0:
                                print("De trap omhoog.")
                            if zaklamp == 0:
                                print("Licht aan.\n")
                            elif zaklamp == 1:
                                pass
                            if zaklamp == 1:
                                print("Zoeken.\n")
                            elif zaklamp == 0:
                                pass
                            print("Selecteer een optie: ")
                            try:
                                    uitweg = input("? ")
                                    if uitweg.lower() == "de trap omhoog":
                                        os.system('cls')
                                        if zaklamp == 1:
                                            os.system('cls')
                                            if codegoed == 0:
                                                print("\033[1;37;40m")
                                                print("U gaat de trap op en komt een dichte deur tegen met een 3 cijferige code.")
                                            elif codegoed == 1:
                                                print("\033[1;37;40m")
                                                print("U gaat de trap op en loopt door de deur.")
                                                time.sleep(3)
                                                
                                            code = input("Code? ")
                                            if code == "248":
                                                print("\033[1;32;40m")
                                                print("Juiste code!")
                                                print("\033[1;37;40m")
                                                codegoed = 1
                                                time.sleep(1)
                                                continue
                                        
                                            elif code != "248":
                                                end_1()
                                                break
                                                
                                            else:
                                                raise OptieError
                                        elif zaklamp == 0:
                                                end_2()
                                                break
                                        
                                            
                                        else:
                                            raise OptieError
                                            
                                    elif uitweg.lower() == "licht aan":
                                        if zaklamp == 0:
                                            os.system('cls')
                                            print("U zoekt naar een lichtbron in de kelder,\nU vind een zaklamp die op de grond lag.")
                                            items_add("Zaklamp")
                                            time.sleep(1)
                                            print("\033[1;35;40m")
                                            print("De zaklamp is toegevoegd aan uw inventaris.")
                                            print("\033[1;37;40m")
                                            zaklamp = 1
                                            time.sleep(3)
                                            continue
                                        elif zaklamp == 1:
                                            os.system('cls')
                                            print("U heeft de zaklamp al.")
                                            time.sleep(1)
                                        else:
                                            raise MenuError
                                    elif uitweg.lower() == "zoeken":
                                        os.system('cls')
                                        print("Zoeken naar items.")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        print(".")
                                        time.sleep(1)
                                        if fles == 0:
                                            os.system('cls')
                                            print("\033[1;32;40m")
                                            print("U heeft een fles gevonden.")
                                            time.sleep(1)
                                            print("\033[1;37;40m")
                                            print("Op de fles staat een etiket:")
                                            print("-------------------")
                                            print("|                 |")
                                            print("|     +++++       |")
                                            print("|      248        |")
                                            print("|     +++++       |")
                                            print("|                 |")
                                            print("-------------------")
                                            fles = 1
                                            time.sleep(1)
                                            items_add("Fles met code 248")
             
             
             
             
                                            print("De fles is toegevoegd aan uw inventaris.")
                                            time.sleep(4)
                                        elif fles == 1:
                                            os.system('cls')
                                            print("\033[1;32;40m")
                                            print("U heeft een sleutel gevonden!")
                                            print("\033[1;37;40m")
                                            time.sleep(1)
                                            items_add("Sleutel")
                                            print("\033[1;35;40m")
                                            print("De sleutel is toegevoegd aan uw inventaris.")
                                            print("\033[1;37;40m")
                                            sleutel = True
                                            fles = 2
                                            time.sleep(4)
                                        elif fles == 2:
                                            os.system('cls')
                                            print("\033[1;32;40m")
                                            print("U heeft batterijen gevonden voor de zaklamp.")
                                            print("\033[1;32;40m")
                                            time.sleep(4)
                                            items_add("Batterijen")
                                            fles = 3
                                            batterijen = True
                                        elif fles == 3:
                                            os.system('cls')
                                            print("\033[1;31;40m")
                                            print("Niks gevonden!")
                                            print("\033[1;32;40m")
                                            time.sleep(4)
                                    elif uitweg.lower() == ("items"):
                                        if len(items) == 0:
                                            print("U heeft niks in uw inventaris...")
                                            time.sleep(1)
                                            continue
                                        else:
                                            print("Items in uw inventaris:")
                                            for i in range(len(items)):
                                                print(items[i])
                                            time.sleep(4)
                                            continue
                                    
                            except:
                                raise MenuError
                        elif codegoed == 1 and einde == 0:
                            if kelder == False and einde == 0:
                                os.system('cls')
                                print("U bevindt zich in een woonkamer.")                       
                                print("Hier ziet u een bureau.")                       
                                print("En een deur die een sleutel nodig heeft.")                    
                                print("De enige opties zijn:\n")
                                print("Loop naar de deur.\nCheck het bureau.\n")
                                print("Selecteer een optie: ")
                            
                                optie2 = input("? ")
                                if optie2.lower() == ("check het bureau"):
                                    os.system('cls')
                                    print("U loopt naar het bureau.")
                                    time.sleep(1)
                                    print("\033[1;37;40m")
                                    print("Op het bureau ligt een stukje papier:")
                                    print("\033[1;34;40m")
                                    print("boek 79")
                                    print("pagina 42")
                                    print("regel 7")
                                    print("\033[1;37;40m")
                                    print("Je pakt het stukje papier op.")
                                    items_add("Stukje papier: (boek 79, pagina 42, regel 7)")
                                    print("\033[1;35;40m")
                                    print("Het stukje papier is toegevoegd aan uw inventaris.")
                                    print("\033[1;37;40m")
                                    time.sleep(5)
                                    continue
                                elif optie2.lower() == ("loop naar de deur"):
                                    if sleutel == True and einde == 0:
                                        os.system('cls')
                                        print("\033[1;32;40m")
                                        print("Deur geopend!")
                                        items_remove("Sleutel")
                                        print("\033[1;37;40m")
                                        time.sleep(4)
                                        while True:
                                            print("\033[1;37;40m")
                                            os.system('cls')
                                            print("U bevindt zich in de bibliotheek.")
                                            print("Hier staan duizenden boeken.")
                                            print("Om te zoeken naar een boek kunt u een nummer invullen.")
                                            print("De enige opties zijn:\n")
                                            print("Boek zoeken.\nrondkijken")
                                            if rondkijken == False:
                                                pass
                                            elif rondkijken == True:
                                                print("Naar de uitgang lopen.\n")
                                            optie3 = input("? ")
                                            if optie3.lower() == ("boek zoeken"):
                                                os.system('cls')
                                                print("Welk boek wilt u zoeken?")
                                                boek = input("? ")
                                                boekint = int(boek)
                                                print("Welke pagina wilt u bekijken?")
                                                pagina = input("? ")
                                                paginaint = int(pagina)
                                                print("Welke regel wilt u lezen?")
                                                regel = input("? ")
                                                regelint = int(regel)
                                                if boekint == 79:
                                                    if paginaint == 42:
                                                        if regelint == 7:
                                                            os.system('cls')
                                                            print("De code is 443463")
                                                            time.sleep(5)
                                                            boekgoed = True
                                                        else:
                                                            os.system('cls')
                                                            print("Deze tekst is onleesbaar...")
                                                            time.sleep(3)
                                                            continue
                                                    else:
                                                        os.system('cls')
                                                        print("Deze tekst is onleesbaar...")
                                                        time.sleep(3)
                                                        continue
                                                else:
                                                    os.system('cls')
                                                    print("Deze tekst is onleesbaar...")
                                                    time.sleep(3)
                                                    continue
                                            elif optie3.lower() == ("rondkijken"):
                                                os.system('cls')
                                                print("U kijkt om zich heen...")
                                                time.sleep(1)
                                                print("Deze bibliotheek lijkt erg verlaten. Er liggen overal boeken en stukjes papier.")
                                                time.sleep(1)
                                                print("Ook zijn bijna alle ramen kapot.")
                                                time.sleep(1)
                                                print("U ziet een groot uitgangsbord links van u.")
                                                time.sleep(1)
                                                print("U volgt het bord en komt een deur tegen met een slot erop.")
                                                time.sleep(4)
                                                rondkijken = True
                                                continue
                                            elif optie3.lower() == ("naar de uitgang lopen") and rondkijken == True:
                                                os.system("cls")
                                                print("De zaklamp valt uit!")
                                                time.sleep(2)
                                                input1 = input("Wilt u nieuwe batterijen in de zaklamp doen?\nY/N? ")
                                                if input1.lower() == ("y"):
                                                    if batterijen == False:
                                                        print("U heeft geen nieuwe batterijen.")
                                                        time.sleep(3)
                                                        end_6()
                                                        break
                                                    else:
                                                        print("U vervangt de batterijen.")
                                                        time.sleep(3)
                                                elif input1.lower() == ("n"):
                                                    end_6()
                                                    break
                                                os.system('cls')
                                                print("Code?")
                                                code2 = input("? ")
                                                if code2 == ("443463"):
                                                    end_4()
                                                    break
                                                else:
                                                    end_1()
                                                    break
                                            elif optie3.lower() == ("items"):
                                                if len(items) == 0:
                                                    print("U heeft niks in uw inventaris...")
                                                    time.sleep(1)
                                                    continue
                                                else:
                                                    print("Items in uw inventaris:")
                                                    for i in range(len(items)):
                                                        print(items[i])
                                                    time.sleep(4)
                                                    continue
                                            elif einde == 0:
                                                break
                                            else:
                                                print("Dat was geen optie!")
                                    elif sleutel == False:
                                        end_3()
                                        break
                                elif optie2.lower() == ("items"):
                                    if len(items) == 0:
                                        print("U heeft niks in uw inventaris...")
                                        time.sleep(1)
                                        continue
                                    else:
                                        print("Items in uw inventaris:")
                                        for i in range(len(items)):
                                            print(items[i])
                                        time.sleep(4)
                                        continue
                                elif kelder == True:
                                    continue
                        elif einde == 0:
                            break                
                elif einde == 0:
                    break       
                                
                                
                else:
                    raise MenuError
            except MenuError:
                os.system('cls')
                print("Dat was geen optie!")
                print("Het programma start nu opnieuw!")
                time.sleep(4)
                continue
            except CodeError:
                os.system('cls')
                print("Die code klopt niet.")
                time.sleep(1)
                continue
            except Ending1:
                os.system('cls')
                print("U viel van de trap af omdat het te donker was.")
                time.sleep(4)
                continue
if einde == 0:
    alles()
