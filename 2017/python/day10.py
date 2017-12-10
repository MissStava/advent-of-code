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




# lengths = [ord(c) for c in '106,118,236,1,130,0,235,254,59,205,2,87,129,25,255,118']
lengths = [ord(c) for c in '1,2,3']
# lengths = [20]
numbers = range(256)
skipSize = 0
currentPosition = 0

lengths.extend([17, 31, 73, 47, 23])

print
print lengths

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

    print numbers

sparseHash = numbers

print
denseHash = []
for x in range(16):
    denseHash.append(reduce(lambda i, j: i ^ j, numbers[:16]))
    numbers = numbers[16:]

denseHashAsHex = [hex(h)[2:] for h in denseHash]
for x in range(16):
    if len(denseHashAsHex[x]) == 1:
        denseHashAsHex[x] = '0'+denseHashAsHex[x]


knottHash = ''.join(denseHashAsHex)

print
print sparseHash
print denseHash
print denseHashAsHex
print knottHash

print
print [reduce(lambda i, j: i ^ j, [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22])]

# 16375e9e032601bd6bafc35c0a03d849 is wrong
# 16375e9e032610bd6bafc35ca003d849
# 37920559104c675143866bd932044c9e
