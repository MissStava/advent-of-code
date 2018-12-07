file = open("input", "r")

ids = [x.strip('\n)') for x in file.readlines()]
# ids = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]

numOfTwos = 0
numOfThrees = 0
for id in ids:
  occurences = dict()
  for letter in id:
    if letter in occurences:
      occurences[letter] += 1
    else:
      occurences[letter] = 1

  if len([k for k,v in occurences.items() if v == 2]) >= 1:
    numOfTwos += 1
    print id

  if len([k for k,v in occurences.items() if v == 3]) >= 1:
    numOfThrees += 1
    print id

print "Day 2 Part 1 = " + str(numOfTwos * numOfThrees)