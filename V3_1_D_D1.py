# Höfundur: Milos Petrovic
# Dagsetning: 26.08.2023
# Verkefni: Forritun 1A - V3_1_D_D1
# Athugasemdir: Ekki athugasemdir
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða
# annars aðila: Já

number = int(input("Tala: "))
counter = 2

if number == 0 or number == 1 or number < 0:
  print(number, "er ekki prímtala")

while counter < number:
  if number % counter == 0:
    print(number, "er ekki prímtala")
    break
  counter += 1

if counter == number:
  print(number, "er prímtala")
