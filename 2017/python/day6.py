state = [11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11]

numberOfStatesSeen = 0
countAtFirstOccurence = 0
countAtSecondOccurence = 0
previousStates = []
stateToWatch = None

while True:

    highestValue = max(state)
    indexOfHighestValue = state.index(highestValue)
    state[indexOfHighestValue] = 0

    columnIndex = indexOfHighestValue
    for n in range(highestValue):
        columnIndex += 1
        if columnIndex == len(state):
            columnIndex =  0

        state[columnIndex] += 1

    numberOfStatesSeen += 1

    if stateToWatch != None and tuple(state) == stateToWatch:
        countAtSecondOccurence = numberOfStatesSeen
        break

    if stateToWatch == None and tuple(state) in previousStates:
        stateToWatch = tuple(state)
        countAtFirstOccurence = numberOfStatesSeen
    else:
        previousStates.append(tuple(state))

print countAtFirstOccurence
# Answer = 4074
print countAtSecondOccurence - countAtFirstOccurence
