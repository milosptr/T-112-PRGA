# Höfundur: Milos Petrovic
# Dagsetning: 26.08.2023
# Verkefni: Forritun 1A - V2_1_C_D1
# Athugasemdir: Ekki athugasemdir
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða
# annars aðila: Já

firstNumber = float(input("Fyrri tala: "))
secondNumber = float(input("Seinni tala: "))

if firstNumber > secondNumber:
  print("Talan", secondNumber, "er minni en", firstNumber)
elif firstNumber < secondNumber:
  print("Talan", firstNumber, "er minni en", secondNumber)
else:
  print("Tölurnar eru jafn stórar")
