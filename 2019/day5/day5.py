file = open("input", "r")
initial_state = map(int, file.read().strip('\n').split(','))

memory = list(initial_state)
address = 0

while True:
    instruction_pointer = address
    instruction = str(memory[instruction_pointer])
    opcode = int(instruction[-2:])
    modes = instruction[:-2][::-1]

    if opcode == 1:
        param1 = memory[instruction_pointer+1]
        param2 = memory[instruction_pointer+2]
        param3 = memory[instruction_pointer+3]
        modes = modes.ljust(2,'0')

        if modes[0] == '1':
            val1 = param1
        else:
            val1 = memory[param1]

        if modes[1] == '1':
            val2 = param2
        else:
            val2 = memory[param2]

        memory[param3] = val1 + val2

        address += 4

    elif opcode == 2:
        param1 = memory[instruction_pointer+1]
        param2 = memory[instruction_pointer+2]
        param3 = memory[instruction_pointer+3]
        modes = modes.ljust(2,'0')

        if modes[0] == '1':
            val1 = param1
        else:
            val1 = memory[param1]

        if modes[1] == '1':
            val2 = param2
        else:
            val2 = memory[param2]

        memory[param3] = val1 * val2

        address += 4

    elif opcode == 3:
        param1 = memory[instruction_pointer+1]
        print "Enter value: "
        memory[param1] = int(input())
        address += 2

    elif opcode == 4:
        param1 = memory[instruction_pointer+1]
        modes = modes.ljust(1,'0')

        if modes[0] == '1':
            val1 = param1
        else:
            val1 = memory[param1]

        print val1
        address += 2

    elif opcode == 5:
        param1 = memory[instruction_pointer+1]
        param2 = memory[instruction_pointer+2]
        modes = modes.ljust(2,'0')

        if modes[0] == '1':
            val1 = param1
        else:
            val1 = memory[param1]

        if modes[1] == '1':
            val2 = param2
        else:
            val2 = memory[param2]

        if val1 != 0:
            address = val2
        else:
            address += 3

    elif opcode == 6:
        param1 = memory[instruction_pointer+1]
        param2 = memory[instruction_pointer+2]
        modes = modes.ljust(2,'0')

        if modes[0] == '1':
            val1 = param1
        else:
            val1 = memory[param1]

        if modes[1] == '1':
            val2 = param2
        else:
            val2 = memory[param2]

        if val1 == 0:
            address = val2
        else:
            address += 3

    elif opcode == 7:
        param1 = memory[instruction_pointer+1]
        param2 = memory[instruction_pointer+2]
        param3 = memory[instruction_pointer+3]
        modes = modes.ljust(2,'0')

        if modes[0] == '1':
            val1 = param1
        else:
            val1 = memory[param1]

        if modes[1] == '1':
            val2 = param2
        else:
            val2 = memory[param2]

        if val1 < val2:
            memory[param3] = 1
        else:
            memory[param3] = 0

        address += 4

    elif opcode == 8:
        param1 = memory[instruction_pointer+1]
        param2 = memory[instruction_pointer+2]
        param3 = memory[instruction_pointer+3]
        modes = modes.ljust(2,'0')

        if modes[0] == '1':
            val1 = param1
        else:
            val1 = memory[param1]

        if modes[1] == '1':
            val2 = param2
        else:
            val2 = memory[param2]

        if val1 == val2:
            memory[param3] = 1
        else:
            memory[param3] = 0

        address += 4

    elif opcode == 99:
        break

if memory[0] == 19690720:
    print 100 * noun + verb

# 15259545 - input 1
# 7616021  - input 5
