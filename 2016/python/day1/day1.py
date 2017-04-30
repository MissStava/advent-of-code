file = open("../inputs/day1.txt", "r")

position = (0, 0)
direction = ((0,1), (1,0), (0,-1), (-1,0))
facing = 0
hqNotFound = True
visitedPositions = []

directions = file.read().split(", ")

for instr in directions:
	if instr[0] == "L":
		facing -= 1
		if facing < 0:
			facing = 3
	else:
		facing += 1
		if facing > 3:
			facing = 0

	for x in range(int(instr[1:])):
		position = (position[0]+direction[facing][0],position[1]+direction[facing][1])
		if hqNotFound:
			if position in visitedPositions:
				hq = position
				hqNotFound = False
			else:
				visitedPositions.append(position)

print position
print hq

# 242
# 150