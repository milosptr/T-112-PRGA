# Höfundur: Milos Petrovic
# Dagsetning: 24.08.2023
# Verkefni: Forritun 1A - V1_1_D_D2
# Athugasemdir: Ekki athugasemdir.
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða
# annars aðila: Já

heightImperial = float(input("Hæð í fetum: "))
weightImperial = float(input("Þyngd í pundum: "))
heightMetric = heightImperial * 0.3048
weightMetric = weightImperial * 0.45
print("BMI:", round(weightMetric / (heightMetric * heightMetric), 2))
