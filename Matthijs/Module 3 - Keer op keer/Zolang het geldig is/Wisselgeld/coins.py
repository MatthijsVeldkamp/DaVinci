# name of student: Matthijs Veldkamp
# number of student:  99071402
# purpose of program: ?
# function of program: ?
# structure of program: ?
nrcoins500 = int(0)
nrcoins200 = int(0)
nrcoins100 = int(0)
nrcoins50 = int(0)
nrcoins20 = int(0)
nrcoins10 = int(0)
nrcoins5 = int(0)
nrcoins2 = int(0)
nrcoins1 = int(0)
toPay = int(float(input('Amount to pay: '))* 100) #
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay #Het aantal van wat je moet betalen word afgetrokken van wat je betaald.
if change > 0: #Als paid en topay hetzelfde zijn gaat het programma verder.
  coinValue = 500 #coinValue wordt veranderd naar 500 zodat het programma over 5 euro vraagt.
  while change > 0 and coinValue > 0: #Dit is wat je moet betalen.
    nrCoins = change // coinValue #het getal word afgerond
    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #
# comment on code below:
    if coinValue == 500:
      nrcoins500 = int(nrCoinsReturned)
      coinValue = 200
    elif coinValue == 200:
      nrcoins200 = int(nrCoinsReturned)
      coinValue = 100
    elif coinValue == 100:
      nrcoins100 = int(nrCoinsReturned)
      coinValue = 50
    elif coinValue == 50:
      nrcoins50 = int(nrCoinsReturned)
      coinValue = 20
    elif coinValue == 20:
      nrcoins20 = int(nrCoinsReturned)
      coinValue = 10
    elif coinValue == 10:
      nrcoins10 = int(nrCoinsReturned)
      coinValue = 5
    elif coinValue == 5:
      nrcoins5 = int(nrCoinsReturned)
      coinValue = 2
    elif coinValue == 2:
      nrcoins2 = int(nrCoinsReturned)
      coinValue = 1
    else:
      nrcoins1 = int(nrCoinsReturned)
      coinValue = 0
if change > 0: #
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')
  print("-----------------------------------")
  print("Munten van 5 euro teruggegeven: "+ str(nrcoins500))
  print("Munten van 2 euro teruggegeven: "+ str(nrcoins200))
  print("Munten van 1 euro teruggegeven: "+ str(nrcoins100))
  print("Munten van 50 eurocent teruggegeven: "+ str(nrcoins50))
  print("Munten van 20 eurocent teruggegeven: "+ str(nrcoins20))
  print("Munten van 10 eurocent teruggegeven: "+ str(nrcoins10))
  print("Munten van 5 eurocent teruggegeven: "+ str(nrcoins5))
  print("Munten van 2 eurocent teruggegeven: "+ str(nrcoins2))
  print("Munten van 1 eurocent teruggegeven: "+ str(nrcoins1))
  print("-----------------------------------")