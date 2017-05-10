import re

file = open("../inputs/day10.txt", "r")

botGiving = {}
botHas = {}
binHas = {}

for line in file:
	line = line.strip()

	firstWord = line.split(' ', 1)[0]

	if firstWord == 'bot':
		result = re.search("([0-9]+)[\D]+(bot|output)\s([0-9]+)[\D]+\s(bot|output)\s([0-9]+)", line)
		giverBot = result.group(1)
		lowReceiverBotType = result.group(2)
		lowReceiverBotValue = result.group(3)
		highReceiverBotType = result.group(4)
		highReceiverBotValue = result.group(5)
		botGiving[giverBot] = (lowReceiverBotType[0]+lowReceiverBotValue, highReceiverBotType[0]+highReceiverBotValue)
	else:
		result = re.search("([0-9]+)[\D]+([0-9]+)", line)
		value = result.group(1)
		receiverBot = result.group(2)

		if receiverBot not in botHas:
			botHas[receiverBot] = []
		botHas[receiverBot].append(value)

actionTaken = False
escapeToken = 0
while True:
	for bot in botHas:
		if len(botHas[bot]) >= 2:
			actionTaken = True

			value1 = int(botHas[bot][0])
			value2 = int(botHas[bot][1])

			if (value1 == 61 and value2 == 17) or (value1 == 17 and value2 == 61):
				print "***"
				print bot
				print "***"

			lowReceiverBot = botGiving[bot][0]
			highReceiverBot = botGiving[bot][1]

			lowReceiverBotType = lowReceiverBot[0]
			lowReceiverBotValue = lowReceiverBot[1:]
			highReceiverBotType = highReceiverBot[0]
			highReceiverBotValue = highReceiverBot[1:]

			if lowReceiverBotType == "o":
				if lowReceiverBotValue not in binHas:
					binHas[lowReceiverBotValue] = []
			else:
				if lowReceiverBot[1:] not in botHas:
					botHas[lowReceiverBot[1:]] = []

			if highReceiverBotType == "o":
				if highReceiverBotValue not in binHas:
					binHas[highReceiverBotValue] = []
			else:
				if highReceiverBot[1:] not in botHas:
					botHas[highReceiverBot[1:]] = []

			if value1 < value2:
				if lowReceiverBotType != "o": 
					botHas[lowReceiverBotValue].append(str(value1))
				else:
					binHas[lowReceiverBotValue].append(str(value1))

				if highReceiverBotType != "o": 
					botHas[highReceiverBot[1:]].append(str(value2))
				else:
					binHas[highReceiverBot[1:]].append(str(value2))

			else:
				if lowReceiverBotType != "o": 
					botHas[lowReceiverBot[1:]].append(str(value2))
				else:
					binHas[lowReceiverBot[1:]].append(str(value2))

				if highReceiverBotType != "o": 
					botHas[highReceiverBot[1:]].append(str(value1))
				else:
					binHas[highReceiverBot[1:]].append(str(value1))

			botHas[bot] = []
			break
	if actionTaken:
		actionTaken = False
	else:
		break

print

# bot 113

print binHas['0']
print binHas['1']
print binHas['2']
# bin 12803