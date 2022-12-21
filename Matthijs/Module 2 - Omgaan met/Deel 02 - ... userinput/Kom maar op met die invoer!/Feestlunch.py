croissantjes = input('Aantal croissantjes ')
stokbroden = input('Aantal stokbroden ')
korting = input('Aantal kortingsbonnen ')
y = float(croissantjes) #Croissantjes
x = float(stokbroden) #stokbroden
z = float(korting) #kortingsbonnen
i=z*0.50
round(i,2)
o=y*0.39
round(o,2)
g=x*2.78
round(g,2)
f=g+o
round(f,2)
u=f-i
round(u,2)
print("De feestlunch kost je bij de bakker" ,round(u,2), "euro voor de" ,a, "croissantjes en de" ,b, "stokbroden als de" ,c, "kortingsbonnon nog geldig zijn!")