file = open("input", "r")
initial_state = map(int, file.read().strip('\n').split(','))

def immediate_mode(modes, pos):
    return len(modes) >= pos+1 and modes[pos] == '1'

def immediate_value(pos):
    return memory[pos]

def position_value(pos):
    return memory[memory[pos]]

memory = list(initial_state)
address = 0
opcode_sizes = {1:4,2:4,3:2,4:2,5:3,6:3,7:4,8:4}

while True:
    instruction_pointer = address
    instruction = str(memory[instruction_pointer])
    opcode = int(instruction[-2:])
    modes = instruction[:-2][::-1]

    if opcode == 1:
        val1 = immediate_value(instruction_pointer+1) if immediate_mode(modes,0) else position_value(instruction_pointer+1)
        val2 = immediate_value(instruction_pointer+2) if immediate_mode(modes,1) else position_value(instruction_pointer+2)
        memory[memory[instruction_pointer+3]] = val1 + val2
        address += opcode_sizes[opcode]

    elif opcode == 2:
        val1 = immediate_value(instruction_pointer+1) if immediate_mode(modes,0) else position_value(instruction_pointer+1)
        val2 = immediate_value(instruction_pointer+2) if immediate_mode(modes,1) else position_value(instruction_pointer+2)
        memory[memory[instruction_pointer+3]] = val1 * val2
        address += opcode_sizes[opcode]

    elif opcode == 3:
        print "Enter value: "
        memory[memory[instruction_pointer+1]] = int(input())
        address += opcode_sizes[opcode]

    elif opcode == 4:
        print immediate_value(instruction_pointer+1) if immediate_mode(modes,0) else position_value(instruction_pointer+1)
        address += opcode_sizes[opcode]

    elif opcode == 5:
        val1 = immediate_value(instruction_pointer+1) if immediate_mode(modes,0) else position_value(instruction_pointer+1)
        val2 = immediate_value(instruction_pointer+2) if immediate_mode(modes,1) else position_value(instruction_pointer+2)
        address = val2 if val1 != 0 else address + opcode_sizes[opcode]

    elif opcode == 6:
        val1 = immediate_value(instruction_pointer+1) if immediate_mode(modes,0) else position_value(instruction_pointer+1)
        val2 = immediate_value(instruction_pointer+2) if immediate_mode(modes,1) else position_value(instruction_pointer+2)
        address = val2 if val1 == 0 else address + opcode_sizes[opcode]

    elif opcode == 7:
        val1 = immediate_value(instruction_pointer+1) if immediate_mode(modes,0) else position_value(instruction_pointer+1)
        val2 = immediate_value(instruction_pointer+2) if immediate_mode(modes,1) else position_value(instruction_pointer+2)
        memory[memory[instruction_pointer+3]] = 1 if val1 < val2 else 0
        address += opcode_sizes[opcode]

    elif opcode == 8:
        val1 = immediate_value(instruction_pointer+1) if immediate_mode(modes,0) else position_value(instruction_pointer+1)
        val2 = immediate_value(instruction_pointer+2) if immediate_mode(modes,1) else position_value(instruction_pointer+2)
        memory[memory[instruction_pointer+3]] = 1 if val1 == val2 else 0
        address += opcode_sizes[opcode]

    elif opcode == 99:
        break

if memory[0] == 19690720:
    print 100 * noun + verb

# 15259545 - input 1
# 7616021  - input 5
