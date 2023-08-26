# Höfundur: Milos Petrovic
# Dagsetning: 26.08.2023
# Verkefni: Forritun 1A - V3_1_C_D1
# Athugasemdir: Ekki athugasemdir
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða
# annars aðila: Já

number = int(input("Tala: "))
originalNumber = number
factorial = 1
step = number < 0 and 1 or -1

while number + step != 0 and number != 0:
  factorial *= number
  number += step

print(originalNumber, "hrópmerkt er", factorial)
