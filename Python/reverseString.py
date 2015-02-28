word = input('Word to reverse: ')

letters = []

for symbol in word:
    letters.append(symbol)

flipped = []

counter = len(letters)

while counter != 0:
    flipped.append(letters[counter-1])
    counter -= 1

backwards = ''.join(flipped)

print('%s reversed is: %s' % (word, backwards))