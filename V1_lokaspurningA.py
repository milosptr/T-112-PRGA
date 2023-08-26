# Höfundur: Milos Petrovic
# Dagsetning: 26.08.2023
# Verkefni: Forritun 1A - V1_lokaspurningA
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

print("Það eru", round(ISK) ,"krónur í eftirfarandi myntum:")
print("1000 x", int(ISK_1000_notes))
print("100 x", int(ISK_100_notes))
print("50 x", int(ISK_50_notes))
print("10 x", int(ISK_10_notes))
print("1 x", int(ISK_1_notes))
