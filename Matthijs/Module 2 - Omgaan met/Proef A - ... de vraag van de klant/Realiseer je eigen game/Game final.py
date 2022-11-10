from slowprint.slowprint import *
import os
# 37 = white, 33 = yellow, 34 = blue, 31 = red, 32 = green.
restart = ("ja")
z = True
codegoed = 0
codegoed = 0
sleutel = False
kelder = False
einde = 0
item1 = str(" ")
item2 = str(" ")
boekgoed = False
rondkijken = False
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
zaklamp = 0
while True:
    if restart.lower() == ("nee"):
        break
    elif einde == 1:
        break
    else:
        print("\033[1;37;40m")
        os.system('cls')
        slowprint("Start:\nStart het spel!\n",0.1)
        slowprint("Instructies:\nEen korte uitleg van hoe het spel werkt.\n",0.1)
        try:
            print("Wat wilt u doen?")
            opties = input("? ")
            if opties.lower() == "instructies":
                os.system('cls')
                print("\033[1;37;40m")
                slowprint("U bevindt zich in de kelder van een groot oud huis, u moet weg zien te komen door de juiste opties te kiezen.",0.1)
                sleep(2)
                slowprint("Wanneer u iets moet typen, staat er (Selecteer een optie:). Typ dan letterlijk de optie over die u wilt kiezen. (Hoofdletters maken niet uit en leestekens hoeft u niet te typen.)",0.1)
                sleep(2)
                slowprint("Gebruik nooit nummers tenzij dat duidelijk gevraagd word.",0.1)
                sleep(2)
                slowprint("Je kan ook altijd items typen om te kijken wat voor items je hebt.",0.1)
                slowprint("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",0.1)
                slowprint("Typ menu om terug te gaan naar het menu.",0.1)
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
                    sleep(3)
                    continue
                    
                    
            
            elif opties.lower() == "start":
                zaklamp = 0
                fles = 0
                os.system('cls')
                print("\033[1;37;40m")
                print("Type uw naam in.")
                name = input("? ")
             
            
                os.system('cls')
                slowprint("Welkom "+name+"", 0.1)
                sleep(0.5)
            
            
                while z == True:
                    if codegoed == 0:
                        os.system('cls')
                        print("\033[1;37;40m")
                        slowprint("U bevindt zich in de kelder van een groot huis.", 0.1)
                        if zaklamp == 0:
                            slowprint("Het is helemaal donker.", 0.1)
                        elif zaklamp == 1:
                            slowprint("U gebruikt de zaklamp om te zien.",0.1)
                        sleep(0.5)
                        slowprint("De enige opties zijn:\n", 0.1)
                        if zaklamp == 1:
                            slowprint("De trap omhoog.", 0.1)
                        elif zaklamp == 0:
                            slowprint("De trap omhoog.", 0.1)
                        if zaklamp == 0:
                            slowprint("Licht aan.\n", 0.1)
                        elif zaklamp == 1:
                            pass
                        if zaklamp == 1:
                            slowprint("Zoeken.\n", 0.1)
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
                                            slowprint("U gaat de trap op en komt een dichte deur tegen met een 3 cijferige code.",0.1)
                                        elif codegoed == 1:
                                            print("\033[1;37;40m")
                                            slowprint("U gaat de trap op en loopt door de deur.")
                                            sleep(2)
                                            
                                        code = input("Code? ")
                                        if code == "248":
                                            print("\033[1;32;40m")
                                            print("Juiste code!")
                                            print("\033[1;37;40m")
                                            codegoed = 1
                                            sleep(1)
                                            continue
                                    
                                        elif code != "248":
                                            print("\033[1;31;40m")
                                            print("Onjuiste code!")
                                            sleep(2)
                                            codegoed = 0
                                            os.system('cls')
                                            print("\033[1;31;40m")
                                            print("-----------------------------------------------")
                                            print("|                                             |")
                                            print("|                   Helaas...                 |")
                                            print("|    U kon niet uit het huis ontsnappen omdat |")
                                            print("|            u de code niet wist.             |")
                                            print("|                                             |")
                                            print("|                Einde 1 van 5                |")
                                            print("|                                             |")
                                            print("-----------------------------------------------")
                                            einde = 1
                                            print("\033[1;37;40m")
                                            sleep(2)
                                            break
                                            
                                        else:
                                            raise OptieError
                                    elif zaklamp == 0:
                                            os.system('cls')
                                            print("\033[1;31;40m")
                                            print("-----------------------------------------------")
                                            print("|                                             |")
                                            print("|                   Helaas...                 |")
                                            print("|          U viel van de trap af omdat        |")
                                            print("|                het te donker was            |")
                                            print("|                                             |")
                                            print("|                Einde 2 van 5                |")
                                            print("|                                             |")
                                            print("-----------------------------------------------")
                                            einde = 1
                                            print("\033[1;37;40m")
                                            sleep(3)
                                            break
                                    
                                        
                                    else:
                                        raise OptieError
                                        
                                elif uitweg.lower() == "licht aan":
                                    if zaklamp == 0:
                                        os.system('cls')
                                        slowprint("U zoekt naar een lichtbron in de kelder,\nU vind een zaklamp die op de grond lag.", 0.1)
                                        zaklamp = 1
                                        sleep(2)
                                        continue
                                    elif zaklamp == 1:
                                        os.system('cls')
                                        print("U heeft de zaklamp al.")
                                        sleep(1)
                                    else:
                                        raise MenuError
                                elif uitweg.lower() == "zoeken":
                                    os.system('cls')
                                    slowprint("Zoeken naar items.",0.1)
                                    sleep(1)
                                    print(".")
                                    sleep(1)
                                    print(".")
                                    sleep(1)
                                    print(".")
                                    sleep(1)
                                    if fles == 0:
                                        os.system('cls')
                                        print("\033[1;32;40m")
                                        slowprint("U heeft een fles gevonden.",0.1)
                                        sleep(1)
                                        print("\033[1;37;40m")
                                        slowprint("Op de fles staat een etiket:",0.1)
                                        slowprint("-------------------",0.1)
                                        slowprint("|                 |",0.1)
                                        slowprint("|     +++++       |",0.1)
                                        slowprint("|      248        |",0.1)
                                        slowprint("|     +++++       |",0.1)
                                        slowprint("|                 |",0.1)
                                        slowprint("-------------------",0.1)
                                        fles = 1
                                        sleep(3)
                                    elif fles == 1:
                                        os.system('cls')
                                        print("\033[1;32;40m")
                                        slowprint("U heeft een sleutel gevonden!",0.1)
                                        print("\033[1;37;40m")
                                        sleutel = True
                                        fles = 2
                                        sleep(3)
                                    elif fles == 2:
                                        os.system('cls')
                                        print("\033[1;31;40m")
                                        slowprint("Niks gevonden!",0.1)
                                        print("\033[1;32;40m")
                                        sleep(3)
                                    elif uitweg.lower() == ("items"):
                                        os.system('cls')
                                        slowprint("Wat u bij u heeft: ")
                                        if zaklamp == 0 & fles == 0 & sleutel == False:
                                            slowprint("U heeft op dit moment geen items.",0.1)
                                            sleep(2)
                                            continue
                                
                                
                        except:
                            raise MenuError
                    elif codegoed == 1:
                        if kelder == False:
                            os.system('cls')
                            slowprint("U bevindt zich in een woonkamer.",0.1)                       
                            slowprint("Hier ziet u een bureau.",0.1)                       
                            slowprint("En een deur die een sleutel nodig heeft.",0.1)                    
                            slowprint("De enige opties zijn:\n",0.1)
                            slowprint("Loop naar de deur.\nCheck het bureau.\n", 0.1)
                            slowprint("Selecteer een optie: ",0.1)
                        
                            optie2 = input("? ")
                            if optie2.lower() == ("check het bureau"):
                                os.system('cls')
                                slowprint("U loopt naar het bureau.",0.1)
                                sleep(1)
                                print("\033[1;37;40m")
                                slowprint("Op het bureau ligt een stukje papier:", 0.1)
                                print("\033[1;34;40m")
                                slowprint("boek 79", 0.1)
                                slowprint("pagina 42", 0.1)
                                slowprint("regel 7", 0.1)
                                print("\033[1;37;40m")
                                sleep(5)
                                continue
                            elif optie2.lower() == ("loop naar de deur"):
                                if sleutel == True:
                                    os.system('cls')
                                    print("\033[1;32;40m")
                                    slowprint("Deur geopend!",0.1)
                                    print("\033[1;37;40m")
                                    sleep(3)
                                    while True:
                                        print("\033[1;37;40m")
                                        os.system('cls')
                                        slowprint("U bevindt zich in de bibliotheek.",0.1)
                                        slowprint("Hier staan duizenden boeken.",0.1)
                                        slowprint("Om te zoeken naar een boek kunt u een nummer invullen.",0.1)
                                        slowprint("De enige opties zijn:\n",0.1)
                                        slowprint("Boek zoeken.\nrondkijken",0.1)
                                        if rondkijken == False:
                                            pass
                                        elif rondkijken == True:
                                            slowprint("Naar de uitgang lopen.\n",0.1)
                                        optie3 = input("? ")
                                        if optie3.lower() == ("boek zoeken"):
                                            os.system('cls')
                                            slowprint("Welk boek wilt u zoeken?",0.1)
                                            boek = input("? ")
                                            boekint = int(boek)
                                            slowprint("Welke pagina wilt u bekijken?",0.1)
                                            pagina = input("? ")
                                            paginaint = int(pagina)
                                            slowprint("Welke regel wilt u lezen?",0.1)
                                            regel = input("? ")
                                            regelint = int(regel)
                                            if boekint == 79:
                                                if paginaint == 42:
                                                    if regelint == 7:
                                                        os.system('cls')
                                                        slowprint("De code is 443463",0.1)
                                                        sleep(5)
                                                        boekgoed = True
                                                    else:
                                                        os.system('cls')
                                                        slowprint("Deze tekst is onleesbaar...",0.1)
                                                        sleep(2)
                                                        continue
                                                else:
                                                    os.system('cls')
                                                    slowprint("Deze tekst is onleesbaar...",0.1)
                                                    sleep(2)
                                                    continue
                                            else:
                                                os.system('cls')
                                                slowprint("Deze tekst is onleesbaar...",0.1)
                                                sleep(2)
                                                continue
                                        elif optie3.lower() == ("rondkijken"):
                                            os.system('cls')
                                            slowprint("U kijkt om zich heen...",0.1)
                                            sleep(1)
                                            slowprint("Deze bibliotheek lijkt erg verlaten. Er liggen overal boeken en stukjes papier.",0.1)
                                            sleep(1)
                                            slowprint("Ook zijn bijna alle ramen kapot.",0.1)
                                            sleep(1)
                                            slowprint("U ziet een groot uitgangsbord links van u.",0.1)
                                            sleep(1)
                                            slowprint("U volgt het bord en komt een deur tegen met een slot erop.",0.1)
                                            sleep(4)
                                            rondkijken = True
                                            continue
                                        elif optie3.lower() == ("naar de uitgang lopen") and rondkijken == True:
                                            os.system('cls')
                                            slowprint("Code?",0.1)
                                            code2 = input("? ")
                                            if code2 == ("443463"):
                                                os.system('cls')
                                                print("\033[1;32;40m")
                                                print("-----------------------------------------------")
                                                print("|                                             |")
                                                print("|                 Goed gedaan                 |")
                                                print("|         U ontsnaptte via de nooduitgang     |")
                                                print("|                                             |")
                                                print("|                Einde 5 van 5                |")
                                                print("|                                             |")
                                                print("-----------------------------------------------")
                                                sleep(5)
                                                einde = 1
                                            else:
                                                os.system('cls')
                                                print("\033[1;31;40m")
                                                print("-----------------------------------------------")
                                                print("|                                             |")
                                                print("|                   Helaas...                 |")
                                                print("|    U kon niet uit het huis ontsnappen omdat |")
                                                print("|            u de code niet wist.             |")
                                                print("|                                             |")
                                                print("|                Einde 1 van 5                |")
                                                print("|                                             |")
                                                print("-----------------------------------------------")
                                                einde = 1
                                                print("\033[1;37;40m")
                                                sleep(5)
                                        else:
                                            slowprint("Dat was geen optie!")
                                elif sleutel == False:
                                    os.system('cls')
                                    print("\033[1;31;40m")
                                    print("-----------------------------------------------")
                                    print("|                                             |")
                                    print("|                   Helaas...                 |")
                                    print("|          U heeft geen sleutel gevonden.     |")
                                    print("|       en kon hierdoor niet de deur openen   |")
                                    print("|                                             |")
                                    print("|                Einde 3 van 5                |")
                                    print("|                                             |")
                                    print("-----------------------------------------------")
                                    einde = 1
                                    print("\033[1;37;40m")
                                    sleep(3)
                                    break
                            elif optie2.lower() == ("items"):
                                os.system('cls')
                                slowprint("Dit zijn de items die u heeft:\n",0.1)
                                if zaklamp == 1:
                                    print("Zaklamp")
                                elif zaklamp != 1:
                                    pass
                                elif zaklamp == 1 & sleutel == True:
                                    print("Zaklamp\nSleutel")
                                else:
                                    print("U heeft geen items...")
                                sleep(5)
                                continue
                            elif kelder == True:
                                continue
                                    
                            
                            
                            
            else:
                raise MenuError
        except MenuError:
            os.system('cls')
            print("Dat was geen optie!")
            print("Het programma start nu opnieuw!")
            sleep(3)
            continue
        except CodeError:
            os.system('cls')
            print("Die code klopt niet.")
            sleep(1)
            continue
        except Ending1:
            os.system('cls')
            print("U viel van de trap af omdat het te donker was.")
            sleep(3)
            continue