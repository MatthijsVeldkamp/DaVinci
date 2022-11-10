#Matthijs Veldkamp, opdracht: PizzaCalculator.
x = True
while x == True:
    import os
    import time
    small = 7.99
    medium = 12.49
    large  = 14.49
    from datetime import date, datetime
    def goto(linenum):
        global line
        line = linenum
    
    print("----------------------------")
    print("|  Small:   7,99  euro  (1)|")
    print("|                          |")
    print("|  Medium:  12.49 euro  (2)|")
    print("|                          |")
    print("|  Large:   14.49 euro  (3)|")
    print("|                          |")
    print("----------------------------")

    try:
        print("(Kies de grootte van de pizza met 1,2 of 3.)")
        grootte = int(input("Grootte van de pizza? "))
        
    except:
        print("Gebruik A.U.B nummers in plaats van letters.")
        break
        
    
      
    try:
        aantal = int(input("Hoeveel pizza's wilt u? "))
        prijs = 0
    except:
        print("Gebruik A.U.B nummers in plaats van letters.")
        break

    x = float(prijs)
    y = float(aantal)
    if grootte == int(1):
        prijs = y * small
        groottepizza = str("Small")
    elif grootte == int(2):
        prijs = y * medium
        groottepizza = str("Medium")
    elif grootte == int(3):
        prijs = y * large
        groottepizza = str("Large")



        



    
    time.sleep(0.5)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("----------------------------------------------")
    print("|    Tijd van bestelling  :" ,current_time,)
    print("----------------------------------------------")
    print("|   ",groottepizza, "pizza               ",aantal,"x|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|    totaal:",str(prijs),"euro")
    print("----------------------------------------------")
    print("|    Bedankt voor uw bestelling!")
    print("----------------------------------------------")

    if y > 15:
        
        print("We hebben niet zoveel pizza. :(")
        time.sleep(2)

    if grootte ==  ("small"):
        print("")

    elif  grootte == ("medium"):
        print("")
        
        
    elif  grootte == ("large"):
        print("")