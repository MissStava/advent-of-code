file = open("day20inputs", "r")
lines = file.read().strip().split('\n')

particles = {}
for x in range(len(lines)):
    line = lines[x]
    parts = line.split(', ')

    p1 = parts[0].strip('p=<').strip('>')
    p2 = parts[1].strip('v=<').strip('>')
    p3 = parts[2].strip('a=<').strip('>')

    particles[x] = {'p': [int(n) for n in p1.split(',')], 'v': [int(n) for n in p2.split(',')], 'a': [int(n) for n in p3.split(',')]}


for x in range(1000):
    closestParticle = ''
    closestDistance = 100000000

    collisions = {}

    for particle in particles:
        particles[particle]['v'][0] += particles[particle]['a'][0]
        particles[particle]['v'][1] += particles[particle]['a'][1]
        particles[particle]['v'][2] += particles[particle]['a'][2]

        particles[particle]['p'][0] += particles[particle]['v'][0]
        particles[particle]['p'][1] += particles[particle]['v'][1]
        particles[particle]['p'][2] += particles[particle]['v'][2]

        if str(particles[particle]['p']) not in collisions:
            collisions[str(particles[particle]['p'])] = []
        collisions[str(particles[particle]['p'])].append(particle)

        distance = abs(particles[particle]['p'][0]) + abs(particles[particle]['p'][1]) + abs(particles[particle]['p'][2])
        if distance < closestDistance:
            closestDistance = distance
            closestParticle = particle

    for collision in collisions:
        if len(collisions[collision]) > 1:
            for particle in collisions[collision]:
                particles.pop(particle)

print closestParticle
print closestDistance
print
# 364

print len(particles)
#420
