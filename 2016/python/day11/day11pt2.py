import heapq

goalState = [[],[],[],["COG","COM","CUG","CUM","DIG","DIM","ELG","ELM","PLG","PLM","PRG", "PRM","RUG","RUM"]]
seenStates = [([["DIG","DIM","ELG","ELM","PRG", "PRM"],["COM","CUM","PLM","RUM"],[]],0)]
statesToTry = ([["DIG","DIM","ELG","ELM","PRG", "PRM"],["COG","CUG","PLG","RUG"],["COM","CUM","PLM","RUM"],[]],0,0)

frontier = []
elevator = 0

heapq.heappush(frontier, (statesToTry, 0))
cost_so_far = {initial: 0}

while frontier:
	state = heapq.heappop(frontier)
	floors, elevator = state

	if floors = goalState:
		break

	items = list(combinations(state[elevator], 2)) + list(combinations(state[elevator], 1))

	if item in floors