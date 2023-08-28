# Höfundur: Milos Petrovic
# Dagsetning: 28.08.2023
# Verkefni: Forritun 1A - V3_1_B_D1
# Athugasemdir: Ekki athugasemdir
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða
# annars aðila: Já

VAT_RATE = 1.24
lowestPrice = int(input("Lægsta verð: "))
highestPrice = int(input("Hæsta verð: "))
stepSize = int(input("Skrefastærð: "))
currentPrice = lowestPrice - stepSize

header1 = "Án skatts"
header2 = "Með skatti"
columnWidth = max(len(header1), len(header2))

print(f"{header1:<{columnWidth}}  {header2}")
while currentPrice + stepSize <= highestPrice:
  currentPrice += stepSize
  priceWithVAT = round(currentPrice * VAT_RATE)
  print(f"{currentPrice:<{columnWidth}d}  {priceWithVAT}")
