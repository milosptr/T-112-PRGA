# Höfundur: Milos Petrovic
# Dagsetning: 24.08.2023
# Verkefni: Forritun 1A - V1_1_A_D2
# Athugasemdir: Ekki athugasemdir.
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða
# annars aðila: Já

capital = float(input("Höfuðstóll: "))
interestRatePercentage = float(input("Vaxtaprósenta: "))
interestRate = interestRatePercentage / 100
years = 3
for i in range(years):
    capital = capital * (1 + interestRate)
print("Höfuðstóll eftir", years, "ár verður þá", round(capital, 2))
