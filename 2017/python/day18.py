file = open("day18inputs", "r")
instructions = file.read().split('\n')

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

registers = {}
toRun = 0
lastSoundPlayed = 0
while True:

    instruction = instructions[toRun]
    cmd = instruction.split()[0]
    reg = instruction.split()[1]

    if reg.isdigit():
        val = instruction.split()[2]
        if reg > 0:
            if is_number(val):
                toRun += int(val)
            else:
                toRun += registers[val]
            continue

    if reg not in registers:
        registers[reg] = 0


    if cmd == 'snd':
        print "Playing sound " + str(registers[reg])
        lastSoundPlayed = registers[reg]

    elif cmd == 'set':
        val = instruction.split()[2]
        if is_number(val):
            registers[reg] = int(val)
        else:
            registers[reg] = registers[val]

    elif cmd == 'add':
        val = instruction.split()[2]
        if is_number(val):
            registers[reg] += int(val)
        else:
            registers[reg] += registers[val]

    elif cmd == 'mul':
        val = instruction.split()[2]
        if is_number(val):
            registers[reg] *= int(val)
        else:
            registers[reg] *= registers[val]

    elif cmd == 'mod':
        val = instruction.split()[2]
        if is_number(val):
            registers[reg] %= int(val)
        else:
            registers[reg] %= registers[val]

    elif cmd == 'rcv':
        if registers[reg] != 0:
            print "Recovers sound " + str(lastSoundPlayed)
            break

    else:
        val = instruction.split()[2]
        if registers[reg] > 0:
            if is_number(val):
                toRun += int(val)
            else:
                toRun += registers[val]
            continue

    toRun += 1
