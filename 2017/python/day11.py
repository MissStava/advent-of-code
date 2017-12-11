file = open("day11inputs", "r")
input = file.read()
steps = input.split(',')

location = (0,0,0)
maxDistance = 0

for step in steps:
    if step == 'n':
        location = (location[0],location[1]+1,location[2]-1)

    elif step == 'ne':
        location = (location[0]+1,location[1],location[2]-1)

    elif step == 'se':
        location = (location[0]+1,location[1]-1,location[2])

    elif step == 's':
        location = (location[0],location[1]-1,location[2]+1)

    elif step == 'sw':
        location = (location[0]-1,location[1],location[2]+1)

    elif step == 'nw':
        location = (location[0]-1,location[1]+1,location[2])

    tempLocation = [abs(n) for n in location]
    tempMaxDistance = max(tempLocation)
    if tempMaxDistance > maxDistance:
        maxDistance = tempMaxDistance

print location
# 764

print maxDistance
# 1532
