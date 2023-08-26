# Höfundur: Milos Petrovic
# Dagsetning: 26.08.2023
# Verkefni: Forritun 1A - V2_lokaspurningA
# Athugasemdir: Ekki athugasemdir
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða
# annars aðila: Já

pricePerSquareMeter = float(input("Fermetraverð: "))
squareMeters = float(input("Fermetrar: "))
price = pricePerSquareMeter * squareMeters
discount = 0

if price < 0:
  print('Negative amount cannot be entered')
  exit()

if price > 500_000:
  discount = 0.05
if price > 1_000_000:
  discount = 0.10

print("Verd:", price)

if discount > 0:
  print("Afsláttur:", price * discount)
  print("Verð með afslætti:", price - (price * discount))
