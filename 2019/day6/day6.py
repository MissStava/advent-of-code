file = open("input", "r")
lines = [line.strip('\n') for line in file.readlines()]

orbits = {}
for line in lines:
    orbitee, orbiter = line.split(')')
    if orbitee not in orbits:
        orbits[orbitee] = []
    if orbiter not in orbits:
        orbits[orbiter] = []
    orbits[orbitee].append(orbiter)

print orbits
