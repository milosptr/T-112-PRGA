# Höfundur: Milos Petrovic
# Dagsetning: 28.08.2023
# Verkefni: Forritun 1A - V4_1_lokaspurningA
# Athugasemdir: Ekki athugasemdir
# Gast þú leyst þetta verkefni án hjálpar (upptöku eða
# annars aðila: Já

icelandicAlphabet = [
    'a', 'á', 'b', 'c', 'd', 'e', 'é', 'f', 'g', 'h', 'i',
    'í', 'j', 'k', 'l', 'm', 'n', 'o', 'ó', 'p', 'q', 'r',
    's', 't', 'u', 'ú', 'v', 'x', 'y', 'ý', 'z', 'þ', 'æ', 'ö'
]

text = input('Textastrengur: ').lower()

for letter in icelandicAlphabet:
    print(letter, text.count(letter))
