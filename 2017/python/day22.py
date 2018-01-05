import numpy as np

current_state = open('day22inputs', 'r').read().strip().split('\n')

leftTurn = {(1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0)}
rightTurn = {(1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0)}

CLEAN = 0
INFECTED = 1
pos = (0,0)
direction = (-1,0)
infected = 0

grid = {}
size = len(current_state)
for row in range(size):
    for col in range(size):
        grid[(row-size/2, col-size/2)] = INFECTED if current_state[row][col] == '#' else CLEAN

for _ in xrange(10000):

    if grid[pos] == CLEAN:
        direction = leftTurn[direction]
        grid[pos] = INFECTED
        infected += 1

    elif grid[pos] == INFECTED:
        direction = rightTurn[direction]
        grid[pos] = CLEAN

    pos = (pos[0] + direction[0], pos[1] + direction[1])
    if pos not in grid:
        grid[pos] = CLEAN


print infected

CLEAN = 0
WEAKENED = 1
INFECTED = 2
FLAGGED = 3
pos = (0,0)
direction = (-1,0)
infected = 0

grid = {}
size = len(current_state)
for row in range(size):
    for col in range(size):
        grid[(row-size/2, col-size/2)] = INFECTED if current_state[row][col] == '#' else CLEAN

for _ in xrange(10000000):

    if grid[pos] == CLEAN:
        direction = leftTurn[direction]
        grid[pos] = WEAKENED

    elif grid[pos] == WEAKENED:
        grid[pos] = INFECTED
        infected += 1

    elif grid[pos] == INFECTED:
        direction = rightTurn[direction]
        grid[pos] = FLAGGED

    elif grid[pos] == FLAGGED:
        direction = (-direction[0], -direction[1])
        grid[pos] = CLEAN

    pos = (pos[0] + direction[0], pos[1] + direction[1])
    if pos not in grid:
        grid[pos] = CLEAN


print infected

# 5339
# 2512380
