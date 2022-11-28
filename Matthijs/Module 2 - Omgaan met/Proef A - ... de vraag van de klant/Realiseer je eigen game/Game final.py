import time
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
        print("Start:\nStart het spel!\n")
        print("Instructies:\nEen korte uitleg van hoe het spel werkt.\n")
        try:
            print("Wat wilt u doen?")
            opties = input("? ")
            if opties.lower() == "instructies":
                os.system('cls')
                print("\033[1;37;40m")
                print("U bevindt zich in de kelder van een groot oud huis, u moet weg zien te komen door de juiste opties te kiezen.")
                time.sleep(2)
                print("Wanneer u iets moet typen, staat er (Selecteer een optie:). Typ dan letterlijk de optie over die u wilt kiezen. (Hoofdletters maken niet uit en leestekens hoeft u niet te typen.)")
                time.sleep(2)
                print("Gebruik nooit nummers tenzij dat duidelijk gevraagd word.")
                time.sleep(2)
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
                    time.sleep(3)
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
                    if codegoed == 0:
                        os.system('cls')
                        print("\033[1;37;40m")
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
                                            time.sleep(2)
                                            
                                        code = input("Code? ")
                                        if code == "248":
                                            print("\033[1;32;40m")
                                            print("Juiste code!")
                                            print("\033[1;37;40m")
                                            codegoed = 1
                                            time.sleep(1)
                                            continue
                                    
                                        elif code != "248":
                                            print("\033[1;31;40m")
                                            print("Onjuiste code!")
                                            time.sleep(2)
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
                                            time.sleep(2)
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
                                            time.sleep(3)
                                            break
                                    
                                        
                                    else:
                                        raise OptieError
                                        
                                elif uitweg.lower() == "licht aan":
                                    if zaklamp == 0:
                                        os.system('cls')
                                        print("U zoekt naar een lichtbron in de kelder,\nU vind een zaklamp die op de grond lag.")
                                        zaklamp = 1
                                        time.sleep(2)
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
                                        time.sleep(3)
                                    elif fles == 1:
                                        os.system('cls')
                                        print("\033[1;32;40m")
                                        print("U heeft een sleutel gevonden!")
                                        print("\033[1;37;40m")
                                        sleutel = True
                                        fles = 2
                                        time.sleep(3)
                                    elif fles == 2:
                                        os.system('cls')
                                        print("\033[1;31;40m")
                                        print("Niks gevonden!")
                                        print("\033[1;32;40m")
                                        time.sleep(3)
                                    elif uitweg.lower() == ("items"):
                                        os.system('cls')
                                        print("Wat u bij u heeft: ")
                                        if zaklamp == 0 & fles == 0 & sleutel == False:
                                            print("U heeft op dit moment geen items.")
                                            time.sleep(2)
                                            continue
                                
                                
                        except:
                            raise MenuError
                    elif codegoed == 1:
                        if kelder == False:
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
                                time.sleep(5)
                                continue
                            elif optie2.lower() == ("loop naar de deur"):
                                if sleutel == True:
                                    os.system('cls')
                                    print("\033[1;32;40m")
                                    print("Deur geopend!")
                                    print("\033[1;37;40m")
                                    time.sleep(3)
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
                                                        time.sleep(2)
                                                        continue
                                                else:
                                                    os.system('cls')
                                                    print("Deze tekst is onleesbaar...")
                                                    time.sleep(2)
                                                    continue
                                            else:
                                                os.system('cls')
                                                print("Deze tekst is onleesbaar...")
                                                time.sleep(2)
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
                                            os.system('cls')
                                            print("Code?")
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
                                                time.sleep(5)
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
                                                time.sleep(5)
                                        else:
                                            print("Dat was geen optie!")
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
                                    time.sleep(3)
                                    break
                            elif optie2.lower() == ("items"):
                                os.system('cls')
                                print("Dit zijn de items die u heeft:\n")
                                if zaklamp == 1:
                                    print("Zaklamp")
                                elif zaklamp != 1:
                                    pass
                                elif zaklamp == 1 & sleutel == True:
                                    print("Zaklamp\nSleutel")
                                else:
                                    print("U heeft geen items...")
                                time.sleep(5)
                                continue
                            elif kelder == True:
                                continue
                                    
                            
                            
                            
            else:
                raise MenuError
        except MenuError:
            os.system('cls')
            print("Dat was geen optie!")
            print("Het programma start nu opnieuw!")
            time.sleep(3)
            continue
        except CodeError:
            os.system('cls')
            print("Die code klopt niet.")
            time.sleep(1)
            continue
        except Ending1:
            os.system('cls')
            print("U viel van de trap af omdat het te donker was.")
            time.sleep(3)
            continue