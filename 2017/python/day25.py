with open("day25inputs", "r") as inputfile:

    input_instructions = [line.strip() for line in inputfile]

current_state = input_instructions.pop(0)[15]
checksum_steps = int(input_instructions.pop(0).split()[5])
instructions = {}
machine = {0: 0}
pos = 0

for s in range(0,60,10):

    state = input_instructions[s + 1].split()[2][0]

    value = int(input_instructions[s + 3].split()[4][0])
    direction = 1 if input_instructions[s + 4].split()[6] == 'right.' else -1
    next_state = input_instructions[s + 5].split()[4][0]
    instructions[state+str(0)] = [value, direction, next_state]

    value = int(input_instructions[s + 7].split()[4][0])
    direction = 1 if input_instructions[s + 8].split()[6] == 'right.' else -1
    next_state = input_instructions[s + 9].split()[4][0]
    instructions[state+str(1)] = [value, direction, next_state]

for _ in range(checksum_steps):
    current_value = machine[pos]
    current_instructions = instructions[current_state+str(current_value)]
    machine[pos] = current_instructions[0]
    pos += current_instructions[1]
    current_state = current_instructions[2]

    if pos not in machine:
        machine[pos] = 0

print sum(machine.values())
# 3554
