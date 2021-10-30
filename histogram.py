counts = dict()
line = input('Enter a line of text: ')
words = line.split()

print('Words', words)
print('Counting...')

for word in words:
  counts[word] = counts.get(word, 0) + 1  #an histogram printing idiom

print('counts', counts)
