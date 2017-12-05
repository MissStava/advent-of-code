file = open("day5inputs", "r")
instructions = file.readlines()
instructionsLen = len(instructions)-1

instructions = [int(ch.rstrip('\n')) for ch in instructions]

nextInstruction = 0
steps = 0
while nextInstruction <= instructionsLen and nextInstruction >= 0:
    offset = instructions[nextInstruction]
    if offset >= 3:
        instructions[nextInstruction] -= 1
    else:
        instructions[nextInstruction] += 1
    nextInstruction += offset
    steps += 1

print steps
# Answer = 342669
# Answer = 25136209
