# Höfundur: Milos Petrovic
# Dagsetning: 28.08.2023
# Verkefni: Forritun 1A - V2_F
# Athugasemdir: Ekki athugasemdir
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða
# annars aðila: Já

exchangeRate = float(input("Hvað eru margar krónur í einum dollara: "))
USD = float(input("Upphæð í dollurum: "))

ISK = exchangeRate * USD
ISK_1000_notes = ISK // 1000
ISK_100_notes = (ISK % 1000) // 100
ISK_50_notes = (ISK % 100) // 50
ISK_10_notes = (ISK % 50) // 10
ISK_1_notes = (ISK % 10) // 1
notes = [
    (1000, ISK_1000_notes),
    (100, ISK_100_notes),
    (50, ISK_50_notes),
    (10, ISK_10_notes),
    (1, ISK_1_notes)
]

print("Það eru", round(ISK) ,"krónur í eftirfarandi myntum:")
for note in notes:
    if(note[1] != 0):
      print(note[0], "x", int(note[1]))
