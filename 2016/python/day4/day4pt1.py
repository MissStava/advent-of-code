import re

file = open("../inputs/day4.txt", "r")

totalSectorId = 0
validRooms = []

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
		validRooms.append((roomName,sectorId))

print totalSectorId

# 173787

unencryptedValidRoomNames = []
for validRoom in validRooms:
	number = int(validRoom[1]) % 26
	unencryptedRoomName = ""
	for letter in validRoom[0]:
		if letter == "-":
			letter = " "
		else:
			letterPos = ord(letter)
			for x in range(number):
				letterPos += 1
				if letterPos > 122:
					letterPos = 97
			letter = chr(letterPos)
		unencryptedRoomName += letter
	unencryptedValidRoomNames.append((unencryptedRoomName,validRoom[1]))

print len(unencryptedValidRoomNames)
print unencryptedValidRoomNames
print [s + " " + str(n) for s, n in unencryptedValidRoomNames if "object" in s]

