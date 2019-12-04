file = open("input", "r")
initial_state = map(int, file.read().strip('\n').split(','))


for noun in range(99):
    for verb in range(99):

        memory = list(initial_state)

        address = 0
        memory[1] = noun
        memory[2] = verb

        while True:
            instruction_pointer = address
            opcode = memory[instruction_pointer]

            if opcode == 1:
                param1 = memory[instruction_pointer+1]
                param2 = memory[instruction_pointer+2]
                param3 = memory[instruction_pointer+3]
                memory[param3] = memory[param1] + memory[param2]
                address += 4

            elif opcode == 2:
                param1 = memory[instruction_pointer+1]
                param2 = memory[instruction_pointer+2]
                param3 = memory[instruction_pointer+3]
                memory[param3] = memory[param1] * memory[param2]
                address += 4

            elif opcode == 99:
                break

        if memory[0] == 19690720:
            print 100 * noun + verb

# 9706670
# 2552
