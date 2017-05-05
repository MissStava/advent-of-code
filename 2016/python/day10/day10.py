import re

file = open("../inputs/day10.txt", "r")

file = ["value 5 goes to bow 2",
		"bot 2 gives low to bot 1 and high to bot 0",
		"value 3 goes to bot 1",
		"bot 1 gives low to output 1 and high to bot 0",
		"bot 0 gives low to output 2 and high to output 0",
		"value 2 goes to bot 2"]

botGiving = {}
botHas = {}

for line in file:
	line = line.strip()

	firstWord = line.split(' ', 1)[0]

	if firstWord == 'bot':
		result = re.search(".+([0-9]+).+([0-9]+).+([0-9]+)", line)
		giverBot = result.group(1)
		lowReceiverBot = result.group(2)
		highReceiverBot = result.group(3)
		botGiving[giverBot] = (lowReceiverBot, highReceiverBot)
	else:
		result = re.search(".+([0-9]+).+([0-9]+)", line)
		value = result.group(1)
		receiverBot = result.group(2)
		if receiverBot not in botHas:
			botHas[receiverBot] = []
		botHas[receiverBot].append(value)

print botGiving
print botHas

for bot in botHas:
	if len(botHas[bot]) == 2:
		lowReceiverBot = botGiving[bot][0]
		highReceiverBot = botGiving[bot][1]

		if lowReceiverBot not in botHas:
			botHas[lowReceiverBot] = []
		if highReceiverBot not in botHas:
			botHas[highReceiverBot] = []
		for value in botHas[bot]:
			if value < 5:
				botHas[lowReceiverBot].append(value)
			else:
				botHas[highReceiverBot].append(value)

print botHas
