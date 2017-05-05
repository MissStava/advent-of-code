import re

line = open("../inputs/day9.txt", "r").read()
newLine = ""

def day9part1(line):
	bracket = re.search("\(([0-9]*)x([0-9]*)\)", line)

	if bracket is None:
		return len(line)

	startPos = bracket.start(0)
	seqSize = int(bracket.group(1))
	repSize = int(bracket.group(2))
	endPos = startPos + len(bracket.group())

	return len(line[:startPos]) + len(line[endPos:endPos+seqSize]) * repSize + day9part1(line[endPos+seqSize:])

print day9part1(line)
# 183269



def day9part2(line):
	bracket = re.search("\(([0-9]*)x([0-9]*)\)", line)

	if bracket is None:
		return len(line)

	startPos = bracket.start(0)
	seqSize = int(bracket.group(1))
	repSize = int(bracket.group(2))
	endPos = startPos + len(bracket.group())

	return len(line[:startPos]) + day9part2(line[endPos:endPos+seqSize]) * repSize + day9part2(line[endPos+seqSize:])

print day9part2(line)
# 11317278863 is too low
