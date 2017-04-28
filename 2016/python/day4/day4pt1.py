import re

file = open("../inputs/day4.txt", "r")

totalSectorId = 0

for line in file:

	checksum = re.search('\[([a-z]{5})\]', line).group(1)
	sectorId = re.search('-([0-9]+)\[', line).group(1)
	roomName = re.search('([a-z-]+)-', line).group(1).replace('-', '')

	letters = {}

	for letter in roomName:
		if letter in letters:
			letters[letter] += 1
		else:
			letters[letter] = 1

	sortedLetters = sorted(letters.items(), key=lambda (k,v): (-v,k))

	concatLetters = ""
	for x in range(5):
		concatLetters += sortedLetters[x][0]

	if concatLetters == checksum:
		totalSectorId += int(sectorId)

print totalSectorId

# 173787