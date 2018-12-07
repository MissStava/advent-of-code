file = open("input", "r")

changes = [int(x.strip('\n)')) for x in file.readlines()]

print "Day 1 Part 1 = " + str(sum(changes))

states = set()
frequency = 0
valueFound = False
while True:
  for change in changes:
    frequency += change
    if frequency in states:
      print "Day 1 Part 2 = " + str(frequency)
      valueFound = True
      break
    states.add(frequency)
  if valueFound:
    break

