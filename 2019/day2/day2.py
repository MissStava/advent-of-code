import copy

file = open("input", "r")
input = file.read().strip('\n')
steps = map(int, input.split(','))


for x in range(99):
    for y in range(99):

        memory = list(steps)

        pos = 0
        memory[1] = x
        memory[2] = y

        while True:
            if memory[pos] == 1:
                memory[memory[pos+3]] = memory[memory[pos+1]] + memory[memory[pos+2]]
            elif memory[pos] == 2:
                memory[memory[pos+3]] = memory[memory[pos+1]] * memory[memory[pos+2]]
            elif memory[pos] == 99:
                break

            pos += 4
            if pos >= len(memory):
                pos = pos - int(len(memory))

        if memory[0] == 19690720:
            print 100 * x + y

# 9706670
