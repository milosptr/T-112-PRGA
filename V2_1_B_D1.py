# Höfundur: Milos Petrovic
# Dagsetning: 26.08.2023
# Verkefni: Forritun 1A - V2_1_B_D1
# Athugasemdir: Ekki athugasemdir
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða
# annars aðila: Já

length = float(input("Lengd ferhyrnings: "))
width = float(input("Breidd ferhyrnings: "))
area = length * width
print("Flatarmál ferhyrnings er", area)

if area < 10:
  print("Ferhyrningur er lítill")
elif area >= 10 and area <= 50:
  print("Meðalstór ferhyrningur")
else:
  print("Stór ferhyrningur")
