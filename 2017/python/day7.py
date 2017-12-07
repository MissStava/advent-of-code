file = open("day7inputs", "r")
lines = file.readlines()

# lines = ['aaaaa (56)', 'bbbbb (104) -> aaaaa, eeeee', 'ccccc (24)', 'ddddd (33)', 'eeeee (18) -> ccccc, ddddd']

nodes = {}

for line in lines:
    components = line.split(' -> ')
    parentAndWeight = components[0]
    parent = parentAndWeight.split()[0]
    weight = parentAndWeight.split()[1]

    nodes[parent] = {'parent':None,'weight':int(weight.replace('(','').replace(')','')), 'children':None}

for line in lines:
    components = line.split(' -> ')
    parentAndWeight = components[0]
    parent = parentAndWeight.split()[0]
    if len(components) == 2:
        children = [c.replace('\n','') for c in components[1].split(', ')]
        for child in children:
            nodes[child]['parent'] = parent
        nodes[parent]['children'] = children

print [k for k,v in nodes.iteritems() if v['parent'] == None]
# Answer = eugwuhl


def setTotalWeights(node):

    totalWeight = 0
    totalWeight += nodes[node]['weight']
    children = nodes[node]['children']
    if children != None:
        childrenWeights = set([])
        for child in children:
            childWeight = setTotalWeights(child)
            childrenWeights.add(childWeight)
            totalWeight += childWeight
        if len(childrenWeights) > 1:
            print str(node) + " " + str(nodes[node]['weight'])
            print totalWeight
            print childrenWeights
            for child in children:
                print str(child) + " " + str(nodes[child]['weight']) + " " + str(nodes[child]['totalWeight'])
            print
    nodes[node]['totalWeight'] = totalWeight

    return totalWeight

print setTotalWeights('eugwuhl')
# 2078 is too high
# 420
