# Check if a word is a Palindrome

word = input('Word to check: ')

letters = []

for symbol in word:
    letters.append(symbol)

flipped = []

counter = len(letters)

while counter != 0:
    flipped.append(letters[counter-1])
    counter -= 1

palindrome = ''.join(flipped)

if palindrome == word:
    print('%s is a palindrome' % (word))

else:
    print('%s is NOT a palindrome' % (word))