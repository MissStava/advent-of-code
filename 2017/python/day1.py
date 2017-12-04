file = open("day1inputs", "r")

chars = list(file.read().rstrip('\n'))
chars.append(chars[0])

print sum([int(chars[n]) for n in list(range(len(chars)-1)) if chars[n] == chars[n+1]])
# Answer = 1177


halfListLen = len(chars)/2
sum = 0
for x in range(len(chars)):
    thisChar = int(chars[x])
    if x >= halfListLen:
        nextChar = int(chars[x-halfListLen])
    else:
        nextChar = int(chars[x+halfListLen])

    if thisChar == nextChar:
        sum += thisChar

print sum
# Answer = 1060
