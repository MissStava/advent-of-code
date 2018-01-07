with open("day24inputs", "r") as inputfile:
    bridges = [map(int, line.strip().split('/')) for line in inputfile]


strengths = []
lengths = []


def find_next(port, other_bridges, strength, length):
    strengths.append(strength)
    lengths.append((strength, length))

    for next_bridge in other_bridges:
        port1 = next_bridge[0]
        port2 = next_bridge[1]

        if port1 == port or port2 == port:
            other_other_bridges = [other_bridge for other_bridge in other_bridges if other_bridge != next_bridge]
            other_port = port1 if port2 == port else port2
            find_next(other_port, other_other_bridges, strength + sum(next_bridge), length+1)

def solve():
    for bridge in bridges:
        port1 = bridge[0]
        port2 = bridge[1]

        if port1 == 0 or port2 == 0:
            other_bridges = [other_bridge for other_bridge in bridges if other_bridge != bridge]
            port = port1 if port2 == 0 else port2
            find_next(port, other_bridges, sum(bridge), 1)

solve()
print max(strengths)
# 2006
longest = max([length[1] for length in lengths])
print max([length[0] for length in lengths if length[1] == longest])
# 1994