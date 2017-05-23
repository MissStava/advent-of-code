import copy
from itertools import combinations

goalState = [[],[],[],["HG","HM","LG","LM"]]
seenStates = [([["HM", "LM"],["HG"],["LG"],[]],0)]
statesToTry = [([["HM", "LM"],["HG"],["LG"],[]],0,0)]

goalState = [[],[],["COG","COM","CUG","CUM","PLG","PLM","PRG", "PRM","RUG","RUM"],[]]
seenStates = [([["PRG", "PRM"],["COG","CUG","PLG","RUG"],["COM","CUM","PLM","RUM"],[]],0)]
statesToTry = [([["PRG", "PRM"],["COG","CUG","PLG","RUG"],["COM","CUM","PLM","RUM"],[]],0,0)]

goalSteps = 0

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

def state_seen_before(state, elevatorAt, seen):
	return True if (state, elevatorAt) in seen else False

def add_seen_state(state, elevatorAt, seen):
	seen.append((state, elevatorAt))

def add_state_to_try(state, elevatorAt, steps, statesToTry):
	statesToTry.append((state, elevatorAt, steps))

def process_move(state, items, elevator, elevatorAt):
	for item in items:
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

		add_seen_state(currentState, elevatorAt, seenStates)
		add_state_to_try(currentState, elevatorAt, steps, statesToTry)
		add_seen_state(currentState, elevatorAt, seenStates)
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
		goalStateFound = process_move(state, items, elevator, elevatorDown)

	if goalStateFound:

		break

print "number of steps = " + str(steps)
