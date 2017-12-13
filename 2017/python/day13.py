file = open("day13inputs", "r")
lines = [line.rstrip('\n') for line in file.readlines()]

def initialiseFirewall(lines):
    firewall = {}
    for line in lines:
        depth = int(line.split(': ')[0])
        rangeNum = int(line.split(': ')[1])
        firewall[depth] = {'range':rangeNum, 'position':0, 'direction':'D'}

    return firewall

def moveScannersOn(firewall):
    for depth in firewall:
        maxRange = firewall[depth]['range']
        position = firewall[depth]['position']
        direction = firewall[depth]['direction']

        if direction == 'D':
            position += 1
            if position == maxRange-1:
                firewall[depth]['direction'] = 'U'
        else:
            position -= 1
            if position == 0:
                firewall[depth]['direction'] = 'D'
        firewall[depth]['position'] = position

detectionPoints = []
for depth in firewall:
    detectionPoints.append((firewall[depth]['range']-1)*2)

print 

delay = 0
while True:
    caughtSeverity = 0
    packetDepth = 0
    waited = 0
    firewall = initialiseFirewall(lines)

    delay += 2

    while packetDepth <= 87:
        if waited > delay:
            packetDepth += 1
            if packetDepth in firewall and firewall[packetDepth]['position'] == 0:
                caughtSeverity += (packetDepth*firewall[packetDepth]['range'])
                break
        else:
            waited += 1

        moveScannersOn(firewall)

    if caughtSeverity == 0:
        print caughtSeverity
        break

print caughtSeverity
# 1904

print delay
# not 2, or 49, or 86, or 73, or 72
