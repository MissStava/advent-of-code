file = open("day11inputs", "r")
input = file.read().strip('\n')
steps = input.split(',')

currentLocation = (0,0,0)
furthestDistance = 0
directionsOf = {'n': (0,1,-1),
              'ne':(1,0,-1),
              'se':(1,-1,0),
              's': (0,-1,1),
              'sw':(-1,0,1),
              'nw':(-1,1,0)}

for step in steps:
    currentLocation = tuple(sum(point) for point in zip(currentLocation, directionsOf[step]))

    distance = max([abs(n) for n in currentLocation])
    if distance > furthestDistance:
        furthestDistance = distance

print max([abs(n) for n in currentLocation])
# 764
print furthestDistance
# 1532
