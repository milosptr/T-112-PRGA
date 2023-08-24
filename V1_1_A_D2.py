# Höfundur: Milos Petrovic
# Dagsetning: 24.08.2023
# Verkefni: Forritun 1A - V1_1_A_D2
# Athugasemdir: Ekki athugasemdir.
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða
# annars aðila: Já

startingTimePoint = float(input("Fyrsti tímapunktur í sekúntum: "))
startingTemperature = float(input("Hiti á fyrsta tímapunkti: "))
middleTimePoint = float(input("Annar tímapunktur í sekúntum: "))
middleTemperature = float(input("Hiti á öðrum tímapunkti: "))
finalTimePoint = float(input("Tímapunktur sem reikna á: "))
finalTemperature = (middleTemperature - startingTemperature)*(finalTimePoint - startingTimePoint)/(middleTimePoint - startingTimePoint) + startingTemperature
print("Hitinn eftir", finalTimePoint, "sekúntur er: ", round(finalTemperature, 2))
