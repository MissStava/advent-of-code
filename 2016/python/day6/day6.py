import collections

file = open("../inputs/day6.txt", "r")

words = file.read().split('\n')

for x in range(8):
	letters = [word[x] for word in words]
	print collections.Counter(letters).most_common(1)[0][0]

# xhnqpqql