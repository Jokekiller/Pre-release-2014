#Harry Robinson
#29/04/2015
#Section B program

ISBN = [13]

for count in range (13):
    count = int(input("PLease enter the next digit of ISBN: "))
    ISBN.append(count)
calculatedDigit = 0
count = 1
while count < 13:
  calculatedDigit = calculatedDigit + ISBN[count]
  count = count + 1
  calculatedDigit = calculatedDigit + ISBN[count] * 3
  count = count + 1
while calculatedDigit >= 10:
  calculatedDigit = calculatedDigit - 10
calculatedDigit = 10 - calculatedDigit
if calculatedDigit == 10:
  calculatedDigit = 0
if calculatedDigit == ISBN[13]:
  print("Valid ISBN")
else:
  print("Invalid ISBN")
