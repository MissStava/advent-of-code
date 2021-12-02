with open('day1.input', 'r') as file:
  lines = [int(row) for row in file]

increments = 0
for n in range(1,len(lines)):
  if lines[n] > lines[n-1]:
    increments += 1

print("Day 1 part 1 answer = " + str(increments))
# 1583

increments = 0
for n in range(len(lines)):
  if (n + 3) > len(lines):
    break

  if sum(lines[n:n+3]) < sum(lines[n+1:n+4]):
    increments += 1


print("Day 1 part 2 answer = " + str(increments))
# 1627