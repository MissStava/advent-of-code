with open('day5.input', 'r') as file:
  data = file.read().splitlines()

nice_lines = 0
for line in data:

  nice = True

  if sum([line.count(v) for v in 'aeiou']) < 3:
    nice = False

  double_chars = 0
  for n in range(len(line) - 1):
    if line[n] == line[n+1]:
      double_chars += 1
  if double_chars < 1:
    nice = False
  
  naughty_combos = ['ab', 'cd', 'pq', 'xy']
  if sum([line.count(v) for v in naughty_combos]) > 0:
    nice = False
  
  if nice:
    nice_lines += 1
  
print("Day 5 part 1 answer = " + str(nice_lines))
# 238