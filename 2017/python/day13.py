file = open("day13inputs", "r")
lines = [line.rstrip('\n') for line in file.readlines()]

firewall = {}
for line in lines:
    depth = int(line.strip().split(': ')[0])
    rangeNum = int(line.strip().split(': ')[1])
    firewall[depth] = rangeNum

def caught(depth, rangeNum):
    return depth % ((rangeNum - 1) * 2) == 0

caughtSeverity = 0
for position in range(87):
    if position not in firewall:
        continue

    depth = position
    rangeNum = firewall[depth]
    if caught(depth, rangeNum):
       caughtSeverity += (depth * rangeNum)

print caughtSeverity
# 1904

delay = 0
while True:
    notCaught = True
    for position in range(87):
        if position not in firewall:
            continue

        depth = position
        rangeNum = firewall[depth]
        if caught(depth + delay, rangeNum):
           notCaught = False
           delay += 1
           break

    if notCaught:
        break

print delay
# 3833504
