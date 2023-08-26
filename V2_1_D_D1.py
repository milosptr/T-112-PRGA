# Höfundur: Milos Petrovic
# Dagsetning: 26.08.2023
# Verkefni: Forritun 1A - V2_1_D_D1
# Athugasemdir: Ekki athugasemdir
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða
# annars aðila: Já

hourlyWage = int(input("Tímakaup: "))
hoursWorked = float(input("Tímafjöldi: "))
bonusCriteria = int(input("Bónusviðmiðun: "))
bonusAmount = 0
salary = hourlyWage * hoursWorked

if hoursWorked > bonusCriteria:
    bonusAmount = int(input("Bónusupphæð: "))
if bonusAmount < 0 or hourlyWage < 0 or hoursWorked < 0 or bonusCriteria < 0:
  print('Negative amount cannot be entered')
  exit()

print("Laun", salary)

if bonusAmount > 0:
  print("Bónus", bonusAmount)
  finalSalary = salary + float(bonusAmount)
  print("heildarlaun", round(finalSalary, 2))
