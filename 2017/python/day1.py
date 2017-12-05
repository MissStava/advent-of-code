file = open("day1inputs", "r")

chars = list(file.read().rstrip('\n'))
chars.append(chars[0])

print sum([int(chars[n]) for n in list(range(len(chars)-1)) if chars[n] == chars[n+1]])
# Answer = 1177

halfListLen = len(chars)/2

sum2 = 0
for x in range(len(chars)):
    thisChar = int(chars[x])
    if x >= halfListLen:
        nextChar = int(chars[x-halfListLen])
    else:
        nextChar = int(chars[x+halfListLen])

    if thisChar == nextChar:
        sum2 += thisChar

print sum2
# Answer = 1060
