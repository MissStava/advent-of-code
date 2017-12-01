file = open("day1inputs", "r")

chars = list(file.read().rstrip('\n'))
chars.append(chars[0])

sum = 0
for x in range(len(chars)-1):
    thisChar = int(chars[x])
    nextChar = int(chars[x+1])
    if thisChar == nextChar:
        sum += thisChar

print sum
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
