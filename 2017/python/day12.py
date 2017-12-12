file = open("day12inputs", "r")
lines = [line.rstrip('\n') for line in file.readlines()]

graph = {}

for line in lines:
    node = int(line.split(' <-> ')[0])
    connectedNodes = [int(n) for n in line.split(' <-> ')[1].split(', ')]

    graph[node] = connectedNodes

nodesInGroup = []
def generate_edges(rootNode):
    for node in graph[rootNode]:
        if node not in nodesInGroup:
            nodesInGroup.append(node)
            generate_edges(node)

groups = []
for node in graph:
    if any(node in group for group in groups):
        continue
    generate_edges(node)
    groups.append(list(set(nodesInGroup)))
    print len(groups[0])
# 288

print len(groups)
# 211
