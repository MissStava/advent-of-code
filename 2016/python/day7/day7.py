import re

file = open("../inputs/day7.txt", "r")

tlsIps = []
sslIps = []

for line in file:
	line = line.strip()

	inBrackets = False
	validLine = False
	for x in range(len(line)-3):
		if line[x] == "[":
			inBrackets = True
		elif line[x] == "]" and inBrackets:
			inBrackets = False

		if line[x] == line[x+3] and line[x+1] == line[x+2] and line[x] != line[x+1] and inBrackets:
			validLine = False
			break
		elif line[x] == line[x+3] and line[x+1] == line[x+2] and line[x] != line[x+1] and not inBrackets:
			validLine = True
	if validLine:
		tlsIps.append(line)

# 105

	inBrackets = False
	validLine = False
	abas = []
	babs = []
	for x in range(len(line)-2):
		if line[x] == "[":
			inBrackets = True
		elif line[x] == "]" and inBrackets:
			inBrackets = False

		if line[x] == line[x+2] and line[x] != line[x+1] and not inBrackets:
			abas.append(line[x]+line[x+1]+line[x+2])
		if line[x] == line[x+2] and line[x] != line[x+1] and inBrackets:
			babs.append(line[x]+line[x+1]+line[x+2])

	if len(abas) > 0 and len(babs) > 0:
		for aba in abas:
			reverseAba = aba[1] + aba[0] + aba[1]
			if reverseAba in babs:
				validLine = True
				break

	if validLine:
		sslIps.append(line)


print len(tlsIps)
print len(sslIps)

# 258
