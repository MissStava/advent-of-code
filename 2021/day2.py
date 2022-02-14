with open('day2.input', 'r') as file:
  instructions = file.read().split("\n")

horizontal = depth = 0
for instruction in instructions:
  action, n = instruction.split(" ")
  n = int(n)

  if action == "forward":
    horizontal += n
  elif action == "up":
    depth -= n
  else:
    depth += n

print("Day 2 part 1 answer = " + str(horizontal * depth))
# 1480518

horizontal = depth = aim = 0
for instruction in instructions:
  action, n = instruction.split(" ")
  n = int(n)

  if action == "forward":
    horizontal += n
    depth += (aim * n)
  elif action == "up":
    aim -= n
  else:
    aim += n

print("Day 2 part 2 answer = " + str(horizontal * depth))
# 1282809906
