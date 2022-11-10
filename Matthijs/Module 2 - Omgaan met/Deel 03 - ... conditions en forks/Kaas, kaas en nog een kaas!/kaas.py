geel = str(input("Is de kaas geel? "))
if geel == ("ja"):
    gaten = str(input("Zitten er gaten in? "))
    if gaten == ("ja"):
        duur = str(input("Is de kaas belagelijk duur? "))
        if duur == ("ja"):
            print("Het is de kaas: Emmenthaler.")
        elif duur == ("nee"):
            print("het is de kaas: Leerdammer.")
        else:
            print("je hebt iets fout ingevuld.")
    elif gaten == ("nee"):
        steen = str(input("Is de kaas hard als steen? "))
        if steen == ("ja"):
            print("Het is de kaas: Parmigiano Reggiano.")
        elif steen == ("nee"):
            print("Het is de kaas: Goudse Kaas.")
        else:
            print("je hebt iets fout ingevuld.")
    else:
            print("je hebt iets fout ingevuld.")
elif geel == ("nee"):
    schimmel = str(input("Heeft de kaas blauwe schimmel? "))
    if schimmel == ("ja"):
        korst = str(input("Heeft de kaas een korst? "))
        if korst == ("ja"):
            print("Het is de kaas: Blue de Rochbaron.")
        elif korst == ("nee"):
            print("Het is de kaas: Foume d'Ambert.")
        else:
            print("je hebt iets fout ingevuld.")
        
    elif schimmel == ("nee"):
        korst2 = str(input("Heeft de kaas een korst? "))
        if korst2 == ("ja"):
            print("Het is de kaas: Camembert.")
        elif korst2 == ("nee"):
            print("Het is de kaas: Mozzarella.")
        else:
            print("je hebt iets fout ingevuld.")
else:
    print("je hebt iets fout ingevuld.")
