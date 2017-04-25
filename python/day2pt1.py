file = open("day2.txt", "r")

pad = [['1', '2', '3'],
	   ['4', '5', '6'],
	   ['7', '8', '9']]

currPos = (1, 1)

movements = {"U": (-1, 0),
			"L": (0, -1),
			"D": (1, 0),
			"R": (0, 1)}

result = ""

for line in file:
	for direction in line.rstrip():
		nextMovement = movements[direction]
		newPos = (currPos[0] + nextMovement[0], currPos[1] + nextMovement[1])
		if newPos[0] < 0 or newPos[0] > 2 or newPos[1] < 0 or newPos[1] > 2:
			continue
		else:
			currPos = newPos

	result += pad[currPos[0]][currPos[1]]

print result


# Part1 = 95549