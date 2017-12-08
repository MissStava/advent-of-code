import operator

file = open("day8inputs", "r")
lines = [l.replace('\n','') for l in file.readlines()]

registers = {}
maxValue = 0

for line in lines:
    # print line

    words = line.split()

    register = words[0]
    incOrDec = words[1]
    amount = int(words[2])
    conditionalRegister = words[4]
    conditional = words[5]
    conditionalAmount = int(words[6])

    if register not in registers:
        registers[register] = 0

    if conditionalRegister not in registers:
        registers[conditionalRegister] = 0

    if conditional == '>':
        if registers[conditionalRegister] > conditionalAmount:
            if incOrDec == 'inc':
                registers[register] += amount
            else:
                registers[register] -= amount

    elif conditional == '>=':
        if registers[conditionalRegister] >= conditionalAmount:
            if incOrDec == 'inc':
                registers[register] += amount
            else:
                registers[register] -= amount

    elif conditional == '!=':
        if registers[conditionalRegister] != conditionalAmount:
            if incOrDec == 'inc':
                registers[register] += amount
            else:
                registers[register] -= amount

    elif conditional == '==':
        if registers[conditionalRegister] == conditionalAmount:
            if incOrDec == 'inc':
                registers[register] += amount
            else:
                registers[register] -= amount

    elif conditional == '<=':
        if registers[conditionalRegister] <= conditionalAmount:
            if incOrDec == 'inc':
                registers[register] += amount
            else:
                registers[register] -= amount

    elif conditional == '<':
        if registers[conditionalRegister] < conditionalAmount:
            if incOrDec == 'inc':
                registers[register] += amount
            else:
                registers[register] -= amount

    else:
        print "conditional error"

    interimMaxKey = max(registers.iteritems(), key=operator.itemgetter(1))[0]
    interimMaxValue = registers[interimMaxKey]

    if interimMaxValue > maxValue:
        maxValue = interimMaxValue


key = max(registers.iteritems(), key=operator.itemgetter(1))[0]
print registers[key]
# 5075

print maxValue
# 7310
