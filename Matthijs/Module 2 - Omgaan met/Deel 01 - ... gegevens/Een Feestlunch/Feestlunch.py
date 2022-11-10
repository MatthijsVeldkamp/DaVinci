a = input(' Aantal croissantjes ')
b = input(' Aantal stokbroden ')
c = input(' Aantal kortingsbonnen ')
y = float(a) #Croissantjes
x = float(b) #stokbroden
z = float(c) #kortingsbonnen
i=z*0.50
o=y*0.39
g=x*2.78
f=g+o
print("Prijs voor de korting=")
print("--------------------------")
print(f)
print("--------------------------")
print("Prijs na de korting=")
print("--------------------------")
u=f-i

print(u)
