
totalStepsInADirection = 1
stepsInDirection = 0
directionChanges = 0
x = 0
y = 0
direction = ('e',(1,0))
numberToFind = 289326

grid = {(0,0): 1}
for n in range(2,numberToFind-1):
# while True:

    x = x + direction[1][0]
    y = y + direction[1][1]

    cellTotal = 0
    if (x-1,y-1) in grid.keys():
        cellTotal += grid[(x-1,y-1)]
    if (x,y-1) in grid.keys():
        cellTotal += grid[(x,y-1)]
    if (x+1,y-1) in grid.keys():
        cellTotal += grid[(x+1,y-1)]
    if (x-1,y) in grid.keys():
        cellTotal += grid[(x-1,y)]
    if (x+1,y) in grid.keys():
        cellTotal += grid[(x+1,y)]
    if (x-1,y+1) in grid.keys():
        cellTotal += grid[(x-1,y+1)]
    if (x,y+1) in grid.keys():
        cellTotal += grid[(x,y+1)]
    if (x+1,y+1) in grid.keys():
        cellTotal += grid[(x+1,y+1)]

    if cellTotal > numberToFind:
        break

    grid[(x,y)] = cellTotal

    stepsInDirection += 1

    if stepsInDirection == totalStepsInADirection:
        if direction[0] == 'e':
            direction = ('n',(0,-1))
        elif direction[0] == 'n':
            direction = ('w',(-1,0))
        elif direction[0] == 'w':
            direction = ('s',(0,1))
        else:
            direction = ('e',(1,0))

        directionChanges += 1
        stepsInDirection = 0

        if directionChanges == 2:
            directionChanges = 0
            totalStepsInADirection += 1

for point in grid:
    print point
print abs(x)+abs(y)
# Answer = 419

print cellTotal
# Answer = 295229
