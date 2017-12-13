file = open("day13inputs", "r")
lines = [line.rstrip('\n') for line in file.readlines()]

firewall = {}
for line in lines:
    depth = int(line.split(': ')[0])
    rangeNum = int(line.split(': ')[1])
    firewall[depth] = {'range':rangeNum, 'detectionPoint':(rangeNum-1)*2}

detectionPoints = []
for depth in firewall:
    detectionPoints.append(((firewall[depth]['range']-1)*2)+depth)

print detectionPoints

delay = 0
while True:
    delay += 10

    found = False

    for x in range(len(detectionPoints)):
        if delay % detectionPoints[x] == 0:
            break
        if x == len(detectionPoints)-1:
            found = True

    if found:
        print delay
        break
