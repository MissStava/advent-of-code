file = open("day2.txt", "r")

pad = [['x', 'x', '1', 'x', 'x'],
	   ['x', '2', '3', '4', 'x'],
	   ['5', '6', '7', '8', '9'],
	   ['x', 'A', 'B', 'C', 'x'],
	   ['x', 'x', 'D', 'x', 'x']]

currPos = (2, 0)

movements = {"U": (-1, 0),
			"L": (0, -1),
			"D": (1, 0),
			"R": (0, 1)}

result = ""

for line in file:
	for direction in line.rstrip():
		nextMovement = movements[direction]
		newPos = (currPos[0] + nextMovement[0], currPos[1] + nextMovement[1])
		if newPos[0] < 0 or newPos[0] > 4 or newPos[1] < 0 or newPos[1] > 4 or pad[newPos[0]][newPos[1]] is 'x':
			continue
		else:
			currPos = newPos

	result += pad[currPos[0]][currPos[1]]

print result


# Part2 = D87AD