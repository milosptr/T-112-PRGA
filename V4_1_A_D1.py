# Höfundur: Milos Petrovic
# Dagsetning: 26.08.2023
# Verkefni: Forritun 1A - V4_1_A_D1
# Athugasemdir: Ekki athugasemdir
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða
# annars aðila: Já

plateNumber = input("Bílnúmer: ").upper()

if len(plateNumber) != 5:
  print("Bílnúmer er ekki rétt")
  exit()

def isLetter(symbol):
  return (ord(symbol) >= 65 and ord(symbol) <= 90)

def isNumber(symbol):
  return ord(symbol) >= 48 and ord(symbol) <= 57

if (not isLetter(plateNumber[0]) or not isLetter(plateNumber[1])):
  print("Tákn 1 og 2 eiga að vera bókstafir")
  exit()

if not(isNumber(plateNumber[2]) or isLetter(plateNumber[2])):
  print("Tákn 3 á að vera bókstafur eða tala")
  exit()

if not(isNumber(plateNumber[3]) and isNumber(plateNumber[4])):
  print("Tákn 4 og 5 eiga að vera tölustafir")
  exit()

print(plateNumber, "er rétt fram sett bílnúmer")
