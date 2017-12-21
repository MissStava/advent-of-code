file = open("day19inputs", "r")
lines = [list(line) for line in file.read().split('\n')]

row = 0
col = 15
direction = (1,0)
letters = []
steps = 0

while True:
    print lines[row][col]
    steps += 1

    if lines[row][col] == '+':
        if lines[row][col+1] != ' ' and direction != (0,-1):
            direction = (0,1)
        elif lines[row][col-1] != ' ' and direction != (0,+1):
            direction = (0,-1)
        elif lines[row-1][col] != ' ' and direction != (1,0):
            direction = (-1,0)
        elif lines[row+1][col] != ' ' and direction != (-1,0):
            direction = (1,0)
    if lines[row][col] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        letters.append(lines[row][col])
        if lines[row][col] == 'Y':
            break

    row += direction[0]
    col += direction[1]

print ''.join(letters)
# GPALMJSOY

print steps
