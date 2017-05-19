import copy
from itertools import combinations

goalState = [[],[],[],["HG","HM","LG","LM"]]
seenStates = []
statesToTry = [([["HM", "LM"],["HG"],["LG"],[]],0,0)]

def validateFloor(floor):
	valid = True
	for item in floor:
		element = item[0]
		component = item[1]
		if component == "M" and element+"G" not in floor and len([x[1] for x in floor if x[1] == 'G']) > 0:
			valid = False
	return valid

goalStateFound = False
goalSteps = 0
while not goalStateFound:
#for j in range(10):

	print statesToTry

	nextStateToTry = statesToTry.pop(0)
	state = nextStateToTry[0]
	elevator = nextStateToTry[1]
	steps = nextStateToTry[2] + 1
	elevatorUp = elevator + 1
	elevatorDown = elevator - 1

	print state

	if elevator < 3:
		currentState = copy.deepcopy(state)
		floor = currentState[elevator]
		floorUp = currentState[elevatorUp]

		for item in floor:

			xCurrentState = copy.deepcopy(currentState)
			xFloor = xCurrentState[elevator]
			xFloorUp = xCurrentState[elevatorUp]

			xFloorUp.append(item)
			xFloorUp = sorted(xFloorUp)
			xFloor.remove(item)

			xCurrentState[elevator] = xFloor
			xCurrentState[elevatorUp] = xFloorUp

			for x in range(4):
				if xCurrentState[x] == None:
					xCurrentState[x] = []

			if xCurrentState == goalState:
				goalStateFound = True
				goalSteps = steps
				print "SUCCESS"
				break


			if xCurrentState in seenStates:
				print "state seen"
				continue
			else:
				seenStates.append((xCurrentState))

			if validateFloor(xFloorUp):
				statesToTry.append((xCurrentState, elevatorUp, steps))

		currentState = copy.deepcopy(state)
		floor = currentState[elevator]
		floorUp = currentState[elevatorUp]

		for items in combinations(floor, 2):

			xCurrentState = copy.deepcopy(currentState)
			xFloor = xCurrentState[elevator]
			xFloorUp = xCurrentState[elevatorUp]

			xFloorUp += items
			xFloorUp = sorted(xFloorUp)
			for item in items:
				xFloor.remove(item)

			xCurrentState[elevator] = xFloor
			xCurrentState[elevatorUp] = xFloorUp

			for x in range(4):
				if xCurrentState[x] == None:
					xCurrentState[x] = []

			if xCurrentState == goalState:
				goalStateFound = True
				goalSteps = steps
				print "SUCCESS"
				break

			if xCurrentState in seenStates:
				print "state seen"
				continue
			else:
				seenStates.append(xCurrentState)

			if validateFloor(xFloorUp):
				statesToTry.append((xCurrentState, elevatorUp, steps))

	if elevator > 0:
		currentState = copy.deepcopy(state)
		floor = currentState[elevator]
		floorDown = currentState[elevatorDown]

		for item in floor:

			xCurrentState = copy.deepcopy(currentState)
			xFloor = xCurrentState[elevator]
			xFloorDown = xCurrentState[elevatorDown]

			xFloorDown.append(item)
			xFloorDown = sorted(xFloorDown)
			xFloor.remove(item)

			xCurrentState[elevator] = xFloor
			xCurrentState[elevatorDown] = xFloorDown

			for x in range(4):
				if xCurrentState[x] == None:
					xCurrentState[x] = []

			if xCurrentState in seenStates:
				print "state seen"
				continue
			else:
				seenStates.append(xCurrentState)

			if validateFloor(xFloorDown):
				statesToTry.append((xCurrentState, elevatorDown, steps))

		currentState = copy.deepcopy(state)
		floor = currentState[elevator]
		floorDown = currentState[elevatorDown]

		for items in combinations(floor, 2):

			xCurrentState = copy.deepcopy(currentState)
			xFloor = xCurrentState[elevator]
			xFloorDown = xCurrentState[elevatorDown]

			xFloorDown += items
			xFloorDown = sorted(xFloorDown)
			for item in items:
				xFloor.remove(item)

			xCurrentState[elevator] = xFloor
			xCurrentState[elevatorDown] = xFloorDown

			for x in range(4):
				if xCurrentState[x] == None:
					xCurrentState[x] = []

			if xCurrentState in seenStates:
				print "state seen"
				continue
			else:
				seenStates.append(xCurrentState)

			if validateFloor(xFloorDown):
				statesToTry.append((xCurrentState, elevatorDown, steps))

print "number of steps = " + str(goalSteps)













# get the first state in the queue
#
# get the items on the current floor of the current state
#
#	what are the possible states that can occur going up
#	
#		is the state the goal state
#
#		has the state been seen before
#		
#		is the state valid
#
#		add state to the queue
#
#	when no valid states added for going up
#	
#		what are the possible states that can occur going down
#
#			has the state been seen before
#		
#			is the state valid
#
#			add state to the queue
