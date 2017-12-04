file = open("day4inputs", "r")
lines = file.readlines()

uniqueLine = 0
sortedUniqueLine = 0
for line in lines:
    wordCount = len(line.split())
    uniqueWordCount = len(set(line.split()))
    sortedUniqueWordCount = len(set([''.join(sorted(a)) for a in line.split()]))

    if wordCount == uniqueWordCount:
        uniqueLine += 1
    if wordCount == sortedUniqueWordCount:
        sortedUniqueLine += 1

print uniqueLine
# Answer = 337

print sortedUniqueLine
# Answer = 231
