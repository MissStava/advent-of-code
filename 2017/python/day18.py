from collections import deque
from collections import defaultdict

file = open("day18inputs", "r")
instructions = [line.split() for line in file.read().split('\n')]

register0 = defaultdict(int)
register1 = defaultdict(int)
register0['p'] = 0
register1['p'] = 1
registers = [register0, register1]
queues = [deque(),deque()]
nextInstructions = [0,0]
state = ["ok", "ok"]

currentProgram = 0
currentRegister = registers[currentProgram]
currentInstruction = nextInstructions[currentProgram]
currentQueue = queues[currentProgram]

totalProg1Sends = 0

def get(s):
    if s in 'abcdefghijklmnopqrstuvwxyz':
        return currentRegister[s]
    return int(s)

while True:

    # print queues

    if instructions[currentInstruction][0] == 'snd':
        val = get(instructions[currentInstruction][1])
        currentQueue.append(val)
        if currentProgram == 1:
            totalProg1Sends += 1

    elif instructions[currentInstruction][0] == 'set':
        reg = instructions[currentInstruction][1]
        val = get(instructions[currentInstruction][2])
        currentRegister[reg] = val

    elif instructions[currentInstruction][0] == 'add':
        reg = instructions[currentInstruction][1]
        val = get(instructions[currentInstruction][2])
        currentRegister[reg] += val

    elif instructions[currentInstruction][0] == 'mul':
        reg = instructions[currentInstruction][1]
        val = get(instructions[currentInstruction][2])
        currentRegister[reg] *= val

    elif instructions[currentInstruction][0] == 'mod':
        reg = instructions[currentInstruction][1]
        val = get(instructions[currentInstruction][2])
        currentRegister[reg] %= val

    elif instructions[currentInstruction][0] == 'rcv':
        if currentProgram == 0:
            if len(queues[1]) > 0:
                reg = instructions[currentInstruction][1]
                val = queues[1].popleft()
                currentRegister[reg] = val
                state[currentProgram] = "ok"
            else:
                if state[1] == "done":
                    print "break 1"
                    break
                if len(queues[0]) == 0 and state[1] == "r":
                    print "break 2"
                    break
                nextInstructions[currentProgram] = currentInstruction
                state[0] = "r"
                currentProgram = 1
                currentInstruction = nextInstructions[currentProgram] - 1
                currentRegister = registers[currentProgram]
                currentQueue = queues[currentProgram]

        else:
            if len(queues[0]) > 0:
                reg = instructions[currentInstruction][1]
                val = queues[0].popleft()
                currentRegister[reg] = val
            else:
                if state[0] == "done":
                    print "break 3"
                    break
                if len(queues[1]) == 0 and state[0] == "r":
                    print "break 4"
                    break
                nextInstructions[currentProgram] = currentInstruction
                state[1] = "r"
                currentProgram = 0
                currentInstruction = nextInstructions[currentProgram] - 1
                currentRegister = registers[currentProgram]
                currentQueue = queues[currentProgram]

    elif instructions[currentInstruction][0] == 'jgz':
        reg = get(instructions[currentInstruction][1])
        if reg > 0:
            val = get(instructions[currentInstruction][2])
            currentInstruction += val - 1

    currentInstruction += 1

    if not 0 <= currentInstruction < len(instructions):
        if state[1-currentProgram] == "done":
            print "break 5"
            break
        state[currentProgram] = "done"
        nextInstructions[currentProgram] = currentInstruction
        currentProgram = 1-currentProgram

        currentInstruction = nextInstructions[currentProgram]
        currentRegister = registers[currentProgram]
# 3188

print totalProg1Sends
# 7112
