with open('day3.input', 'r') as file:
  data = file.read().replace('\n', '')

directions = {
  '^': (0, 1),
  'v': (0, -1),
  '<': (-1, 0),
  '>': (1, 0),
}

def add_tuples(tuple1, tuple2):
  return tuple(map(sum, zip(tuple1, tuple2)))

def santas_turn(count):
  return count % 2 == 0

def calculate_santa_stops(data):
  current_coords = (0, 0)
  visited_cords = {current_coords}

  for direction in data:
    current_coords = add_tuples(current_coords, directions[direction])
    visited_cords.add(current_coords)
  
  return len(visited_cords)

def calculate_santa_and_robo_stops(data):
  santa_coords = (0, 0)
  robo_coords = (0, 0)
  visited_cords = {santa_coords}

  for count, direction in enumerate(data):
    if santas_turn(count):
      current_coords = santa_coords
    else:
      current_coords = robo_coords

    current_coords = add_tuples(current_coords, directions[direction])
    visited_cords.add(current_coords)

    if santas_turn(count):
      santa_coords = current_coords
    else:
      robo_coords = current_coords
  
  return len(visited_cords)


print("Part 1 answer = {}".format(calculate_santa_stops(data)))
print("Part 2 answer = {}".format(calculate_santa_and_robo_stops(data)))
