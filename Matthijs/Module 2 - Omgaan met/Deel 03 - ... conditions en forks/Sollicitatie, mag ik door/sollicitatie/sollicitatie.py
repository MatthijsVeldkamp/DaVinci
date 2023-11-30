import os
import time
while True:
    errors = []
    os.system('cls')
    print("Wat is uw naam?")
    naam = input("? ")
    os.system('cls')
    print("Welkom",naam,)
    print("------------------------------------------")
    print("|                                        |")
    print("| U gaat een aantal vragen beantwoorden. |")
    print("| Hierna ziet u of u mag solliciteren.   |")
    print("|                                        |")
    print("|          veel Succes!                  |")
    print("|                                        |")
    print("------------------------------------------")
    while True:
        os.system('cls')
        gender = str(input("Bent u een man of vrouw? ")).lower()
        if gender.lower() == "man":
            geslacht = 1
            break
        elif gender.lower() == "vrouw":
            geslacht = 2
            break
        else:
            print("Er ging iets fout.")
            time.sleep(1)
    check = 0
    print("Hoeveel jaar ervaring heeft u met jongleren?")
    jongleren = input("? ")
    jonglerenfloat = float(jongleren)
    if jonglerenfloat > 5:
        check += 1
    else:
        check += 0
        errors.append("U heeft te weinig ervaring met jongleren.")
    print("Hoeveel jaar praktijkervaring heeft u met acrobatiek?")
    acrobatiek = input("? ")
    acrobatiekfloat = float(acrobatiek)
    if acrobatiekfloat > 3:
        check += 1
    else:
        errors.append("U heeft te weinig ervaring met acrobatiek.")

    print("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?")
    praktijk = input("? ")
    floatpraktijk = float(praktijk)
    if floatpraktijk > 4:
        check += 1
    else:
        check += 0
        errors.append("U heeft te weinig ervaring met dieren-dressuur.")
    diploma = str(input("Heeft u een MBO-4 diploma ondernemen? "))
    if diploma.lower() == "ja":
        check += 1
   
    elif diploma.lower() == "nee":
        check += 0
        errors.append("U heeft geen MBO-4 diploma.")
    else:
        print("Er ging iets fout.")
        break

    certificaat = str(input("Heeft u het certificaat overleven met gevaarlijk personeel? "))
    if certificaat.lower() == "ja":
        check += 1
    elif certificaat.lower() == "nee":
        check += 0
        errors.append("U heeft geen certificaat overleven met gevaarlijk personeel.")
    else:
        print("Er ging iets fout.")
        break


    
    rijbewijs = str(input("Heeft u een vrachtwagen rijbewijs? "))
    if rijbewijs.lower() == "ja":
        check += 1
   
    elif rijbewijs.lower() == "nee":
        check += 0
        errors.append("U heeft geen vrachtwagen rijbewijs.")
    else:
        print("Er ging iets fout.")
        break
    
    hoed = str(input("Heeft u een hoge hoed? "))
    if hoed.lower() == "ja":
        check += 1
    
    elif hoed.lower() == "nee":
        check += 0
        errors.append("U heeft geen hoge hoed.")
    else:
        print("Er ging iets fout.")
        break
    
    if geslacht == 1:
        print("Wat is uw snorlengte in centimeters?")
        snor = input("? ")
        floatsnor = float(snor)
        if floatsnor > 10:
            check += 1
        
        else:
            check += 0
            errors.append("U heeft geen snor of uw snor is te kort.")
    elif geslacht == 2:
        print("Wat is uw krulhaarlengte in centimeters?")
        haar = input("? ")
        floathaar = float(haar)
        if floathaar > 20:
            check += 1
        
        else:
            check += 0
            errors.append("U heeft geen krulhaar of uw krulhaar is te kort.")
    print("Wat is uw gewicht in hele kg?")
    kilo = input("? ")
    floatkilo = float(kilo)
    if floatkilo >= 90 and floatkilo <= 120:
        check += 1
        
    else:
        check += 0
        errors.append("U gewicht voldoet niet.")
    print("Wat is uw lengte in hele cm?")
    lengte = input("? ")
    floatlengte = float(lengte)
    if floatlengte > 150:
        check += 1
    
    else:
        check += 0
        errors.append("U bent te klein.")

    if check == 9 and len(errors) == 0:
        os.system('cls')
        print("-------------------------------------------")
        print("|            Gefeliciteerd!               |")
        print("|                                         |")
        print("|                                         |")
        print("|          U mag solliciteren             |")
        print("-------------------------------------------")
        time.sleep(5)
        os.system('cls')
        break
    else:
        os.system('cls')
        print("Helaas, u mag niet solliciteren. U heeft niet aan alle eisen voldaan\nen u heeft de volgende fouten gemaakt:")
        for i in errors:
            print(i)
        time.sleep(5)
        break