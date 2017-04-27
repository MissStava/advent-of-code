file = open("../inputs/day3.txt", "r")

validTriangles = 0

elements = [int(x) for x in file.read().replace('\n', ' ').split()]

for x in range(0,len(elements),9):
	for y in range(3):
		if elements[x+y+0] + elements[x+y+3] > elements[x+y+6] and elements[x+y+3] + elements[x+y+6] > elements[x+y+0] and elements[x+y+6] + elements[x+y+0] > elements[x+y+3] :
			validTriangles += 1

print validTriangles

# Part 2 answer is 1839
