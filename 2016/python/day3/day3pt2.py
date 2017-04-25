file = open("day3.txt", "r")

validTriangles = 0

elements = [int(x) for x in file.read().replace('\n', ' ').split()]


for line in file:
	side1, side2, side3 = [int(x) for x in line.split()]

	if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
		validTriangles += 1

print validTriangles

# Part1 = 1032