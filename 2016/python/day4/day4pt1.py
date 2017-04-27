import re

# file = open("../inputs/day4.txt", "r")

# for line in file:

string = "bnmrtldq-fqzcd-bqxnfdmhb-bgnbnkzsd-zmzkxrhr-105[bdnzm]"

checksum = re.search('\[([a-z]{5})\]', string).group(1)
sectorId = re.search('-([0-9]+)\[', string).group(1)
roomName = re.search('([a-z-]+)-', string).group(1).replace('-', '')

letters = {}

for letter in roomName:
	if letter in letters:
		letters[letter] += 1
	else:
		letters[letter] = 1



print letters
print sorted(letters, key=letters.__getitem__, reverse=True)

