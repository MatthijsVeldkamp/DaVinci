woord = input("Woord?: ")
print(woord + " "+ woord)
print(woord + woord)
newWoord = ''
for letter in woord:
    newWoord += letter+letter

print(woord[::-1])