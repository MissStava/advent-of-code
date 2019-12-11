file = open("input", "r")
lines = [line.strip('\n') for line in file.readlines()]

orbits = {}
for line in lines:
    parent, child = line.split(')')
    orbits[child] = parent

def count_orbits(node, count):
    if node == 'COM':
        return count
    count += 1
    return count_orbits(orbits[node], count)

def get_key(graph, val):
    return [key for key, value in graph.items() if val == value]

def bfs(graph, start, end):
    queue = [[start]]
    visited = []

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            neighbours = get_key[graph, node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == end:
                    return new_path

            visited.append(node)
    return None



print sum([count_orbits(node, 0) for node in orbits])
# 162816

print bfs(orbits, 'YOU', 'SAN')
