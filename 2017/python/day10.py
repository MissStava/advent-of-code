lengths = [106,118,236,1,130,0,235,254,59,205,2,87,129,25,255,118]
# lengths = [20]
numbers = range(256)
skipSize = 0
currentPosition = 0

for length in lengths:

    numbersToReverse = []
    loopPosition = currentPosition
    for num in range(length):
        if loopPosition == len(numbers):
            loopPosition = 0

        numbersToReverse.append(numbers[loopPosition])

        loopPosition += 1

    numbersToReverse.reverse()
    loopPosition = currentPosition
    for num in numbersToReverse:
        if loopPosition == len(numbers):
            loopPosition = 0

        numbers[loopPosition] = num

        loopPosition += 1

    if currentPosition + length + skipSize <= 255:
        currentPosition += length + skipSize
    else:
        currentPosition = currentPosition + length + skipSize - 256

    skipSize += 1

print numbers[:2]
print numbers[0] * numbers[1]
# 6909


lengths = [ord(c) for c in '106,118,236,1,130,0,235,254,59,205,2,87,129,25,255,118']
numbers = range(256)
skipSize = 0
currentPosition = 0

lengths.extend([17, 31, 73, 47, 23])

for round in range(64):
    for length in lengths:
        numbersToReverse = []
        loopPosition = currentPosition
        for num in range(length):
            numbersToReverse.append(numbers[loopPosition])

            loopPosition += 1
            if loopPosition == len(numbers):
                loopPosition = 0

        numbersToReverse.reverse()
        loopPosition = currentPosition
        for num in numbersToReverse:
            numbers[loopPosition] = num

            loopPosition += 1
            if loopPosition == len(numbers):
                loopPosition = 0

        currentPosition += length + skipSize
        while currentPosition > 255:
            currentPosition -= 256

        skipSize += 1

denseHash = []
for x in range(16):
    denseHash.append(reduce(lambda i, j: i ^ j, numbers[:16]))
    numbers = numbers[16:]

denseHashAsHex = [hex(h)[2:] for h in denseHash]
for x in range(16):
    if len(denseHashAsHex[x]) == 1:
        denseHashAsHex[x] = '0'+denseHashAsHex[x]

print ''.join(denseHashAsHex)
# 9d5f4561367d379cfbf04f8c471c0095
