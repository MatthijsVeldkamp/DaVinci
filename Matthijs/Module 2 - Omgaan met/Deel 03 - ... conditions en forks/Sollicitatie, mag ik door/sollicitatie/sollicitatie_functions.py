def vraag_met_eis(bericht:str,eis:int) -> int:
    print(bericht)
    result = input("? ")
    try:
        if int(result) >= eis:
            return result
    except ValueError:
        print("Dat is geen geldig antwoord.")
        return "error"

def vraag_met_twee_eisen(bericht:str,eis:int,eis2:int) -> int:
    print(bericht)
    result = input("? ")
    try:
        if int(result) >= eis and int(result) <= eis2:
            return result
    except ValueError:
        print("Dat is geen geldig antwoord.")
        return "error"
    
def vraag(bericht:str) -> str:
    print(bericht)
    return input("? ").lower()

def vraag_met_list(bericht:str,lijst:list) -> str:
    print(bericht)
    result = input("? ").lower()
    if result in lijst:
        return result
    else:
        print("Dat is geen geldig antwoord.")
        return "error"