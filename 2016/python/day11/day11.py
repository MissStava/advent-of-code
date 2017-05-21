import copy
from itertools import combinations

goalState = [[],[],[],["HG","HM","LG","LM"]]
seenStates = [[["HM", "LM"],["HG"],["LG"],[]]]
statesToTry = [([["HM", "LM"],["HG"],["LG"],[]],0,0)]
# statesToTry = [([[], ['HM'], ['HG', 'LG', 'LM'], []], 1, 0)]

def is_state_valid(state):
	for floor in state:
		for item in floor:
			element = item[0]
			component = item[1]

			if component == "M" and element+"G" not in floor and len([x[1] for x in floor if x[1] == 'G']) > 0:
				return False
	return True

def fill_empty_floors(state):
	for x in range(4):
		if state[x] == None:
			state[x] = []
	return state

def move_items_and_sort(state, items, elevatorStart, elevatorStop):
	state[elevatorStop] += items
	for item in items:
		state[elevatorStart].remove(item)
	state[elevatorStart] = sorted(state[elevatorStart])
	state[elevatorStop] = sorted(state[elevatorStop])

# goalStateFound = False
# goalSteps = 0
# while not goalStateFound:
# # for j in range(4):

# 	print "statesToTry = " + str(statesToTry)

# 	nextStateToTry = statesToTry.pop(0)
# 	state = nextStateToTry[0]
# 	elevator = nextStateToTry[1]
# 	steps = nextStateToTry[2] + 1
# 	elevatorUp = elevator + 1
# 	elevatorDown = elevator - 1

# 	if elevator < 3 and not goalStateFound:

# 		currentState = copy.deepcopy(state)
# 		floor = currentState[elevator]
# 		floorUp = currentState[elevatorUp]
# 		multiItemMoved = False

# 		for items in combinations(floor, 2):

# 			xCurrentState = copy.deepcopy(currentState)
# 			xFloor = xCurrentState[elevator]
# 			xFloorUp = xCurrentState[elevatorUp]

# 			move_items_and_sort(xCurrentState, items, elevator, elevatorUp)

# 			fill_empty_floors(xCurrentState)

# 			if (items, xFloorUp) in seenStates:
# 				continue
# 			else:
# 				if isStateValid(xCurrentState):
# 					if xCurrentState == goalState:
# 						goalStateFound = True
# 						goalSteps = steps
# 						print "SUCCESS"
# 						break

# 					print "xCurrentState = " + str(xCurrentState)
# 					print "goalState = " + str(goalState)
# 					print "steps = " + str(steps)
# 					print
# 					statesToTry.append((xCurrentState, elevatorUp, steps))
# 					seenStates.append((items, xFloorUp))
# 					multiItemMoved = True

# 		if goalStateFound:
# 			break

# 		if not multiItemMoved:
# 			currentState = copy.deepcopy(state)
# 			floor = currentState[elevator]
# 			floorUp = currentState[elevatorUp]

# 			for item in floor:

# 				xCurrentState = copy.deepcopy(currentState)
# 				xFloor = xCurrentState[elevator]
# 				xFloorUp = xCurrentState[elevatorUp]

# 				move_items_and_sort(xCurrentState, [item], elevator, elevatorUp)

# 				fill_empty_floors(xCurrentState)

# 				if (item, xFloorUp) in seenStates:
# 					continue
# 				else:
# 					if isStateValid(xCurrentState):
# 						if xCurrentState == goalState:
# 							goalStateFound = True
# 							goalSteps = steps
# 							print "SUCCESS"
# 							break

# 						print "xCurrentState = " + str(xCurrentState)
# 						print "goalState = " + str(goalState)
# 						print "steps = " + str(steps)
# 						print

# 						statesToTry.append((xCurrentState, elevatorUp, steps))
# 						seenStates.append((item, xFloorUp))

# 	if elevator > 0 and not goalStateFound:

# 		currentState = copy.deepcopy(state)
# 		floor = currentState[elevator]
# 		floorDown = currentState[elevatorDown]
# 		multiItemMoved = False

# 		for items in combinations(floor, 2):

# 			xCurrentState = copy.deepcopy(currentState)
# 			xFloor = xCurrentState[elevator]
# 			xFloorDown = xCurrentState[elevatorDown]

# 			move_items_and_sort(xCurrentState, items, elevator, elevatorDown)

# 			fill_empty_floors(xCurrentState)

# 			if (item, floorDown) in seenStates:
# 				continue
# 			else:
# 				if isStateValid(xCurrentState):
# 					if xCurrentState == goalState:
# 						goalStateFound = True
# 						goalSteps = steps
# 						print "SUCCESS"
# 						break

# 					statesToTry.append((xCurrentState, elevatorDown, steps))
# 					seenStates.append((item, floorDown))
# 					multiItemMoved = True
		
# 		if goalStateFound:
# 			break

# 		if not multiItemMoved:
# 			currentState = copy.deepcopy(state)
# 			floor = currentState[elevator]
# 			floorDown = currentState[elevatorDown]

# 			for item in floor:

# 				xCurrentState = copy.deepcopy(currentState)
# 				xFloor = xCurrentState[elevator]
# 				xFloorDown = xCurrentState[elevatorDown]
d
# 				move_items_and_sort(xCurrentState, [item], elevator, elevatorDown)

# 				fill_empty_floors(xCurrentState)

# 				if (item, floorDown) in seenStates:
# 					continue
# 				else:
# 					if isStateValid(xCurrentState):					
# 						if xCurrentState == goalState:
# 							goalStateFound = True
# 							goalSteps = steps
# 							print "SUCCESS"
# 							break

# 						statesToTry.append((xCurrentState, elevatorDown, steps))
# 						seenStates.append((item, floorDown))		

# print "number of steps = " + str(goalSteps)
