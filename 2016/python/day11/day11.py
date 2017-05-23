import copy
from itertools import combinations

goalState = [[],[],[],["HG","HM","LG","LM"]]
seenStates = [([["HM", "LM"],["HG"],["LG"],[]],0)]
statesToTry = [([["HM", "LM"],["HG"],["LG"],[]],0,0)]

goalState = [[],[],[],["COG","COM","CUG","CUM","PLG","PLM","PRG", "PRM","RUG","RUM"]]
seenStates = [([["PRG", "PRM"],["COG","CUG","PLG","RUG"],["COM","CUM","PLM","RUM"],[]],0)]
statesToTry = [([["PRG", "PRM"],["COG","CUG","PLG","RUG"],["COM","CUM","PLM","RUM"],[]],0,0)]

passesMade = 0

goalSteps = 0

def is_state_valid(state):
	for floor in state:
		for item in floor:
			element = item[:2]
			component = item[-1]

			if component == "M" and element+"G" not in floor and len([x[-1] for x in floor if x[-1] == 'G']) > 0:
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

def state_seen_before(state, elevatorAt, seen):
	return True if (state, elevatorAt) in seen else False

def add_seen_state(state, elevatorAt, seen):
	seen.append((state, elevatorAt))

def add_state_to_try(state, elevatorAt, steps, statesToTry):
	statesToTry.append((state, elevatorAt, steps))

def item_is_a_pair(item):
	return True if len(item) == 2 and item[0][:2] == item[1][:2] else False

def process_move(state, items, elevator, elevatorAt):
	validDoubleAdded = False
	# pairAlreadyMoved = False
	for item in items:

		if len(item) == 1 and validDoubleAdded and elevatorAt > elevator:
			break

		currentState = copy.deepcopy(state)
		move_items_and_sort(currentState, item, elevator, elevatorAt)
		fill_empty_floors(currentState)

		if state_seen_before(currentState, elevatorAt, seenStates):
			continue

		if not is_state_valid(currentState):
			continue
			
		if currentState == goalState:
			goalSteps = steps
			print "SUCCESS"
			return True
			break

		# if item_is_a_pair(item) and pairAlreadyMoved:
		# 	continue

		add_seen_state(currentState, elevatorAt, seenStates)
		add_state_to_try(currentState, elevatorAt, steps, statesToTry)
		add_seen_state(currentState, elevatorAt, seenStates)

		if len(item) == 2:
			validDoubleAdded = True
		# if item_is_a_pair(item):
		# 	pairAlreadyMoved = True
	return False

while True:

	# print "statesToTry = " + str(statesToTry)

	nextStateToTry = statesToTry.pop(0)
	state = nextStateToTry[0]
	elevator = nextStateToTry[1]
	steps = nextStateToTry[2] + 1
	elevatorUp = elevator + 1
	elevatorDown = elevator - 1
	items = list(combinations(state[elevator], 2)) + list(combinations(state[elevator], 1))
	goalStateFound = False

	if elevator < 3 and not goalStateFound:
		goalStateFound = process_move(state, items, elevator, elevatorUp)

	if elevator > 0 and not goalStateFound:

		itemsBelow = 0
		for floor in range(elevator):
			itemsBelow += len(state[floor])

		if itemsBelow > 0:
			goalStateFound = process_move(state, items, elevator, elevatorDown)

	passesMade += 1
	if passesMade % 100 == 0:
		print str(passesMade) + " " + str(len(statesToTry))

	if goalStateFound:
		print "statesToTry = " + str(statesToTry)
		print "state = " + str(nextStateToTry)
		break

print "number of steps = " + str(steps)

# 24 is too low
# 33!