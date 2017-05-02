import collections

file = open("../inputs/day6.txt", "r")

words = file.read().split('\n')

password = ""
for x in range(8):
	letters = [word[x] for word in words]
	password += collections.Counter(letters).most_common(1)[0][0]
print password

password = ""
for x in range(8):
	letters = [word[x] for word in words]
	password += collections.Counter(letters).most_common()[-1][0]
print password

# xhnqpqql
# brhailro