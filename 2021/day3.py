with open('Advent2021Day3.txt', 'r') as file:
  lines = file.read().split("\n")

gamma = epsilon = ""

for n in range(len(lines[0])):
  if sum([int(line[n]) for line in lines]) >= (len(lines)/2):
    gamma += "1"
    epsilon += "0"
  else:
    gamma += "0"
    epsilon += "1"

print("Day 3 part 1 answer = " + str(int(gamma, 2) * int(epsilon, 2)))
# 738234

oxygen = co2 = lines

for n in range(len(lines[0])):
  if len([line for line in oxygen if line[n] == "1"]) >= len(oxygen)/2:
    common = "1"
  else:
    common = "0"
  
  oxygen = [line for line in oxygen if line[n] == common]
  if len(oxygen) == 1:
    break
print("Oxygen = " + oxygen[0])

for n in range(len(lines[0])):
  if len([line for line in co2 if line[n] == "0"]) <= len(co2)/2:
    common = "0"
  else:
    common = "1"
  
  co2 = [line for line in co2 if line[n] == common]
  if len(co2) == 1:
    break
print("Co2 = " + co2[0])
  
print("Day 3 part 2 answer = " + str(int(oxygen[0], 2) * int(co2[0], 2)))
# 3969126