# Höfundur: Milos Petrovic
# Dagsetning: 28.08.2023
# Verkefni: Forritun 1A - V4_1_C
# Athugasemdir: Ekki athugasemdir
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða
# annars aðila: Já

columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rows = ['1', '2', '3', '4', '5', '6', '7', '8']

knightPosition = input("Reitur sem riddari er á: ")
currentColumn = columns.index(knightPosition[0].lower())
currentRow = int(knightPosition[1]) - 1 # -1 því við erum að nota index
possibleMoves = []

knightMoves = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]

for move in knightMoves:
  column = currentColumn + move[0]
  row = currentRow + move[1]

  if(column >= 0 and column < len(columns) and row >= 0 and row < len(rows)):
    possibleMoves.append(columns[column] + rows[row])

sortedPossibleMoves = possibleMoves.sort()

print("Riddari á a1 kemst á reiti:")
for move in possibleMoves:
  print(move)
