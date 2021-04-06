with open('day1.input', 'r') as file:
  data = file.read().replace('\n', '')

UP = '('
DOWN = ')'

final_floor = data.count(UP) - data.count(DOWN)
print("Part 1 answer = {}".format(final_floor))

current_floor = 0
for count, value in enumerate(data, 1):
  if value == UP:
    current_floor += 1
  else:
    current_floor -= 1

  if current_floor < 0:
    print("Part 2 answer = {}".format(count))
    break