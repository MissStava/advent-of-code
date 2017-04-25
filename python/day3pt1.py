file = open("day3.txt", "r")

validTriangles = 0

for line in file:
	side1, side2, side3 = [int(x) for x in line.split()]

	if side1 + side2 > side3 :
		validTriangles += 1

print validTriangles

# Part1 = 1032