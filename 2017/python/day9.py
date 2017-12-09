file = open("day9inputs", "r")

text = file.read()

while text.find('!') != -1:
    idx = text.find('!')
    text = text[:idx] + text[idx+2:]

numOfGarbageChars = 0

while text.find('<') != -1:
    startOfGarbage = text.find('<')
    endOfGarbage = text.find('>')
    text = text[:startOfGarbage] + text[endOfGarbage+1:]
    numOfGarbageChars += (endOfGarbage-1 - startOfGarbage)

startOfAGroup = 0
score = 0
groups = 0

for s in text:
    if s == '{':
        startOfAGroup += 1
    elif s == '}':
        groups += 1
        score += startOfAGroup
        startOfAGroup -= 1

print text
print groups

print score
#16869

print numOfGarbageChars
#7284
