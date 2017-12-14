grid = []
for n in range(128):
    lengths = [ord(c) for c in list('ffayrhll-'+str(n))]
    lengths.extend([17, 31, 73, 47, 23])
    numbers = range(256)
    skipSize = 0
    currentPosition = 0

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

    knotHash = ''.join(denseHashAsHex)
    knotHashAsBinary = ''.join([bin(int(h,16))[2:].zfill(4) for h in knotHash])

    grid.append([int(k) for k in list(knotHashAsBinary)])

total = 0
for line in grid:
    total += sum(line)

print total
# 8190

def invalidCell(x, y):
    return (x, y) in visited or not grid[x][y]

visited = set()
def dfs(x, y):
    if invalidCell(x, y):
        return
    visited.add((x, y))

    if x > 0:
        dfs(x-1, y)
    if y > 0:
        dfs(x, y-1)
    if x < 127:
        dfs(x+1, y)
    if y < 127:
        dfs(x, y+1)

count = 0
for y in xrange(128):
    for x in xrange(128):
        if invalidCell(x, y):
            continue
        count += 1
        dfs(x, y)

print count
# 1134
