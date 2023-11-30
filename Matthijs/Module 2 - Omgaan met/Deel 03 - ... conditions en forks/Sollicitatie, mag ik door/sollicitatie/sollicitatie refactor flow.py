from sollicitatie_functions import *
errors = []
print("Welkom, u gaat een aantal vragen beantwoorden. Hierna ziet u of u mag solliciteren.\nVeel succes!")
naam = vraag("Wat is je naam?")
print(f"Welkom {naam}")
gender = None

while gender == None:
    gender = vraag_met_list("Bent u een man of vrouw?",["man","vrouw","m","v"])

while True:
    jongleren = vraag_met_eis("Hoeveel jaar ervaring heeft u met jongleren?",5)
    if jongleren == None:
        errors.append("U heeft te weinig ervaring met jongleren.")
        break
    elif jongleren != None and jongleren != "error":
        break

while True:
    acrobatiek = vraag_met_eis("Hoeveel jaar praktijkervaring heeft u met acrobatiek?",3)
    if acrobatiek == None:
        errors.append("U heeft te weinig ervaring met acrobatiek.")
        break
    elif acrobatiek != None and acrobatiek != "error":
        break

while True:
    praktijk = vraag_met_eis("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?",4)
    if praktijk == None:
        errors.append("U heeft te weinig ervaring met dieren-dressuur.")
        break
    elif praktijk != None and praktijk != "error":
        break

while True:
    diploma = vraag_met_list("Heeft u een MBO-4 diploma ondernemen?",["ja","nee"])
    if diploma == "nee":
        errors.append("U heeft geen MBO-4 diploma ondernemen.")
        break
    elif diploma != None and diploma != "error":
        break

while True:
    certificaat = vraag_met_list("Heeft u het certificaat overleven met gevaarlijk personeel?",["ja","nee"])
    if certificaat == "nee":
        errors.append("U heeft geen certificaat overleven met gevaarlijk personeel.")
        break
    elif certificaat != None and certificaat != "error":
        break

while True:
    rijbewijs = vraag_met_list("Heeft u een geldig vrachtwagen rijbewijs?",["ja","nee"])
    if rijbewijs == "nee":
        errors.append("U heeft geen geldig vrachtwagen rijbewijs.")
        break
    elif rijbewijs != None and rijbewijs != "error":
        break

while True:
    hoed = vraag_met_list("Heeft u een hoge hoed?",["ja","nee"])
    if hoed == "nee":
        errors.append("U heeft geen hoge hoed.")
        break
    elif hoed != None:
        break

if gender in ["man","m"]:
    while True:
        snor = vraag_met_eis("Wat is uw snorlengte in centimeters?",10)
        if snor == None:
            errors.append("U heeft geen snor of uw snor is te kort.")
            break
        elif snor != None and snor != "error":
            break
else:
    while True:
        krulhaar = vraag_met_eis("Wat is uw krulhaarlengte in centimeters?",20)
        if krulhaar == None:
            errors.append("U heeft geen krulhaar of uw krulhaar is te kort.")
            break
        elif krulhaar != None and krulhaar != "error":
            break

while True:
    gewicht = vraag_met_twee_eisen("Wat is uw gewicht in kilogram?",90,120)
    if gewicht == None:
        errors.append("Uw gewicht voldoet niet.")
        break
    elif gewicht != None and gewicht != "error":
        break

while True:
    lengte = vraag_met_eis("Wat is uw lengte in centimeters?",150)
    if lengte == None:
        errors.append("U bent te klein.")
        break
    elif lengte != None and lengte != "error":
        break

while True:
    certificaat = vraag_met_list("Heeft u het certificaat overleven met gevaarlijk personeel?",["ja","nee"])
    if certificaat == None:
        errors.append("U heeft geen certificaat overleven met gevaarlijk personeel.")
        break
    elif certificaat != None:
        break

if len(errors) > 0:
    print("U voldoet niet aan de eisen.")
    print("De volgende punten zijn niet goed:")
    for error in errors:
        print(error)
else:
    print("U voldoet aan de eisen.\nGefeliciteerd, u mag solliciteren!")