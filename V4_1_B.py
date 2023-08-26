# Höfundur: Milos Petrovic
# Dagsetning: 26.08.2023
# Verkefni: Forritun 1A - V4_1_B
# Athugasemdir: Ekki athugasemdir
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða
# annars aðila: Já
shouldLoop = True

while shouldLoop:
  text = input("Textastrengur: ")
  searchQuery = input("Tákn sem leita á að: ")
  counter = text.count(searchQuery)
  #
  # Alternative solution using find() method
  #
  # counter = 0
  # index = text.find(searchQuery)
  # while index != -1:
  #   counter += 1
  #   index = text.find(searchQuery, index + 1)
  #
  print("Táknið a kemur",counter ,"sinnum fyrir í þessum texta")

  shouldStop = input("Endurtaka? (J eða j ef já): ")
  if shouldStop != "j" and shouldStop != "J":
    shouldLoop = False
