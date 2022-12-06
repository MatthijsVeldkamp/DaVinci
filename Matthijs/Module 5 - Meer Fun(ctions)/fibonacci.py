# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946
getallen = [0]
def optellen(hoeveel:int):
    a = 0 #variables om mee te beginnen.
    b = 1 #variables om mee te beginnen.
    som = a + b
    getallen.append(som) #som wordt toegevoegd aan de lijst [getallen].
    for i in range(hoeveel): #Hoe vaak de gebruiker het wilt.
        volgende = getallen.append(getallen[a]+getallen[b])
        a += 1
        b += 1
    return print(getallen)
optellen(hoeveel=int(input("Hoeveel? ")))