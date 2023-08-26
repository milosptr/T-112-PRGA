# Höfundur: Milos Petrovic
# Dagsetning: 26.08.2023
# Verkefni: Forritun 1A - V1_2_A_D1
# Athugasemdir: Ekki athugasemdir
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða
# annars aðila: Já

days = int(input("Dagafjöldi: "))
years = days // 365
weeks = days % 365 // 7
days = days % 365 % 7
print("ár:", years)
print("vikur:", weeks)
print("dagar:", days)
