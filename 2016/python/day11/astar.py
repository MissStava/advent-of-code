def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far


came_from, cost_so_far = a_star_search(diagram4, (1, 4), (7, 8))
draw_grid(diagram4, width=3, point_to=came_from, start=(1, 4), goal=(7, 8))
print()
draw_grid(diagram4, width=3, number=cost_so_far, start=(1, 4), goal=(7, 8))






from itertools import combinations
import heapq

# hardcoded input
polonium, thulium, promethium, ruthenium, cobalt, elerium, dilithium = 1, 2, 3, 4, 5, 6, 7
initial = (0, (
    tuple(sorted((polonium, thulium, -thulium, promethium, ruthenium, -ruthenium, cobalt, -cobalt, elerium, -elerium, dilithium, -dilithium))),
    tuple(sorted((-polonium, -promethium))), (), ()
))

def correct(floor):
    if not floor or floor[-1] < 0: # no generators
        return True
    return all(-chip in floor for chip in floor if chip < 0)

frontier = []
heapq.heappush(frontier, (0, initial))
cost_so_far = {initial: 0}

while frontier:
    _, current = heapq.heappop(frontier)
    floor, floors = current
    if floor == 3 and all(len(f) == 0 for f in floors[:-1]): # goal!
        break

    directions = [dir for dir in (-1, 1) if 0 <= floor + dir < 4]
    moves = list(combinations(floors[floor], 2)) + list(combinations(floors[floor], 1))
    for move in moves:
        for direction in directions:
            new_floors = list(floors)
            new_floors[floor] = tuple(x for x in floors[floor] if x not in move)
            new_floors[floor+direction] = tuple(sorted(floors[floor+direction] + move))

            if not correct(new_floors[floor]) or not correct(new_floors[floor+direction]):
                continue

            next = (floor+direction, tuple(new_floors))
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost - len(new_floors[3])*10 # silly manually tweakable heuristic factor
                heapq.heappush(frontier, (priority, next))

print(cost_so_far[current], current)