# Höfundur: Milos Petrovic
# Dagsetning: 26.08.2023
# Verkefni: Forritun 1A - V3_1_A_D1
# Athugasemdir: Ekki athugasemdir
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða
# annars aðila: Já

loop = True

while loop:
  firstNumber = float(input("Fyrri tala: "))
  secondNumber = float(input("Seinni tala: "))
  print("Summa talnanna er: ", firstNumber + secondNumber)
  shouldContinue = input("Viltu endurtaka? (j eða J ef já, annars eitthvað annað) ")
  if shouldContinue != "j" and shouldContinue != "J":
    loop = False
