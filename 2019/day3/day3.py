file = open("input", "r")
wires = file.readlines()

directions = {'U':(0,1),'D':(0,-1),'L':(-1,0),'R':(1,0)}

grid1 = []
grid2 = []
crossover = []
pos = (0,0)
steps = 0

for move in wires[0].split(','):
    direction = move[:1]
    distance = int(move[1:])

    new_pos = pos
    for m in range(distance):
        new_pos = new_pos + directions[direction]
        # if direction == 'U':
        #     # new_pos = (new_pos[0],new_pos[1]+1)
        # elif direction == 'D':
        #     new_pos = (new_pos[0],new_pos[1]-1)
        # elif direction == 'L':
        #     new_pos = (new_pos[0]-1,new_pos[1])
        # else:
        #     new_pos = (new_pos[0]+1,new_pos[1])

        steps += 1

        grid1.append({new_pos:steps})
    pos = new_pos

pos = (0,0)
steps = 0

for move in wires[1].split(','):
    direction = move[:1]
    distance = int(move[1:])

    new_pos = pos
    for m in range(distance):
        if direction == 'U':
            new_pos = (new_pos[0],new_pos[1]+1)
        elif direction == 'D':
            new_pos = (new_pos[0],new_pos[1]-1)
        elif direction == 'L':
            new_pos = (new_pos[0]-1,new_pos[1])
        else:
            new_pos = (new_pos[0]+1,new_pos[1])

        steps += 1

        grid2.append({new_pos:steps})
    pos = new_pos


print min([abs(a)+abs(b) for (a,b) in set([k for d in grid1 for k in d.keys()]) & set([k for d in grid2 for k in d.keys()])])
# 245

steps2 = []
intersections = [(a,b) for (a,b) in set([k for d in grid1 for k in d.keys()]) & set([k for d in grid2 for k in d.keys()])]
for intersection in intersections:
    # print intersection
     steps2.append(sum([item[intersection] for item in grid1 if intersection in item.keys()] + [item[intersection] for item in grid2 if intersection in item.keys()]))
print min(steps2)
# 48262
