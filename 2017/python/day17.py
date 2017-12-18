steps = 377

# buffer = [0]
currentPosition = 0

for n in range(1,50000001):

    currentPosition = (currentPosition + steps) % n + 1
    # while currentPosition >= len(buffer):
    #     currentPosition -= len(buffer)
    # currentPosition += 1

    if currentPosition == 1:
        print n

    # buffer.insert(currentPosition, n)

# print buffer[currentPosition+1]
# 596
# 39051595
