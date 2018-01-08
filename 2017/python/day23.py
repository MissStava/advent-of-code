from collections import defaultdict

file = open("day23inputs", "r")
instructions = [line.split() for line in file.read().split('\n')]

registers = defaultdict(int)
for reg in 'abcdefgh':
    registers[reg] = 0

invoked = 0
currentInstruction = 0

def get(s):
    if s in 'abcdefgh':
        return registers[s]
    return int(s)

while True:

    if instructions[currentInstruction][0] == 'set':
        reg = instructions[currentInstruction][1]
        val = get(instructions[currentInstruction][2])
        registers[reg] = val

    elif instructions[currentInstruction][0] == 'sub':
        reg = instructions[currentInstruction][1]
        val = get(instructions[currentInstruction][2])
        registers[reg] -= val

    elif instructions[currentInstruction][0] == 'mul':
        reg = instructions[currentInstruction][1]
        val = get(instructions[currentInstruction][2])
        registers[reg] *= val
        invoked += 1

    elif instructions[currentInstruction][0] == 'jnz':
        reg = get(instructions[currentInstruction][1])
        if reg != 0:
            val = get(instructions[currentInstruction][2])
            currentInstruction += val - 1


    currentInstruction += 1
    if not 0 <= currentInstruction < len(instructions)-1:
        break

print invoked
# 3025

# b = c = 57
# if a != 0:
#   b *= 100 + 100000 # 105700
#   c = b + 17000     # 122700

h = 0
for b in range(105700, 122700, 17):
  f = 1
  for d in range(2, b+1):
    for e in range(2, b+1):
      if d * e == b:
        f = 0
        break
    if f == 0:
        break

  if f == 0:
    h += 1

print h
# 915
