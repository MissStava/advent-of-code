import re

file = open("input", "r")

claims = [x.strip('\n)') for x in file.readlines()]
# claims = ['#1379 @ 930,208: 28x11', '#1380 @ 290,693: 25x25', '#1381 @ 252,661: 20x17']
# claims = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']

fabric = dict()
claimSizes = dict()

for claim in claims:
  m = re.search('#(\d{1,4})\s@\s(\d*,\d*):\s(\d*x\d*)', claim)
  id = m.group(1)
  left, top = m.group(2).split(',')
  width, height = m.group(3).split('x')

  for x in range(1 + int(top), int(top) + int(height) + 1):
    for y in range(1 + int(left), int(left) + int(width) + 1):
      pos = str(x) + "," + str(y)
      if pos in fabric:
        fabric[pos] = 'X'
      else:
        fabric[pos] = id

  claimSizes[id] = int(width) * int(height)

print "Day 3 Part 1 = " + str(len([k for k,v in fabric.items() if v == 'X']))

for kk in claimSizes:
  if len([k for k,v in fabric.items() if v == kk]) == claimSizes[kk]:
    print "Day 3 Part 2 = " + str(kk)
    break