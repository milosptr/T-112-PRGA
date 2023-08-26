# Höfundur: Milos Petrovic
# Dagsetning: 26.08.2023
# Verkefni: Forritun 1A - V1_2_B_D1
# Athugasemdir: Ekki athugasemdir
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða
# annars aðila: Já

seconds = int(input("Sekúntur: "))
hours = seconds // 3600
minutes = seconds % 3600 // 60
seconds = seconds % 3600 % 60
print("klst:", hours)
print("mín:", minutes)
print("sek:", seconds)
