file = open("day16inputs", "r")
moves = file.read().split(',')

positions = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']

seen = []
for x in range(100):

    s = ''.join(positions)
    if s in seen:
        print s
        print seen[1000000000 % x]
        break
    seen.append(s)

    for move in moves:
        if move[0] == 's':
            amountToSpin = int(move[1:])
            positions = positions[-amountToSpin:] + positions[:-amountToSpin]

        elif move[0] == 'x':
            posA = int(move[1:].split('/')[0])
            posB = int(move[1:].split('/')[1])
            positions[posA], positions[posB] = positions[posB], positions[posA]

        else:
            progA, progB = move[1:].split('/')
            progAPos = positions.index(progA)
            progBPos = positions.index(progB)
            positions[progAPos], positions[progBPos] = positions[progBPos], positions[progAPos]

    print x

print ''.join(positions)
# lgpkniodmjacfbeh
# hklecbpnjigoafmd
