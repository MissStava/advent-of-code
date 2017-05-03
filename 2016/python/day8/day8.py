file = open("../inputs/day8.txt", "r")

display = [[".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		   [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		   [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		   [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		   [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
		   [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]

instrs = ["rect 3x2", "rotate column x=1 by 1", "rotate row y=0 by 4"]
for instr in file:
	if "rect" in instr:
		rect = instr.split()[1].split('x')
		x = int(rect[1])
		y = int(rect[0])

		for row in range(x):
			for col in range(y):
				display[row][col] = "#"

	if "rotate column" in instr:
		col = int(instr.split()[2].split('=')[1])
		pixels = int(instr.split()[4])

		for num in range(pixels):

			elements = []
			for num2 in range(len(display)):
				elements.append(display[num2][col])

			for num2 in range(1,len(display)):
				display[num2][col] = elements[num2-1]
			display[0][col] = elements[-1]

	if "rotate row" in instr:
		row = int(instr.split()[2].split('=')[1])
		pixels = int(instr.split()[4])

		for num in range(pixels):

			elements = []
			for num2 in range(len(display[0])):
				elements.append(display[row][num2])

			for num2 in range(1,len(display[0])):
				display[row][num2] = elements[num2-1]
			display[row][0] = elements[-1]
	
	for x in range(len(display)):
		print display[x]
	print

print sum(x.count('#') for x in display)