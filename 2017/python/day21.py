import numpy as np

file = open("day21inputs", "r")
lines = file.read().strip().split('\n')

def string_to_array(s):
    return np.array([[c == '#' for c in l]
                     for l in s.split('/')])

def resize(x, boxSize):
    return x * (boxSize + 1) // boxSize

def perform_enhancement(art_grid):
    size = len(art_grid)
    box_size = 2 if size % 2 == 0 else 3
    new_size = resize(size, box_size)
    new_box_size = box_size + 1

    solution = np.empty((new_size, new_size), dtype=bool)
    squares = range(0, size, box_size)
    new_squares = range(0, new_size, new_box_size)

    for start_x, stop_x in zip(squares, new_squares):
        for start_y, stop_y in zip(squares, new_squares):
            square = art_grid[start_x:start_x+box_size, start_y:start_y+box_size]
            enhanced = mappings[square.tobytes()]
            solution[stop_x:stop_x+new_box_size, stop_y:stop_y+new_box_size] = enhanced
    return solution

def solve(iterations):
    art_grid = string_to_array('.#./..#/###')

    for _ in range(iterations):
        art_grid = perform_enhancement(art_grid)
    return int(art_grid.sum())

mappings = {}
for line in lines:
    pattern, outcome = map(string_to_array, line.strip().split(' => '))
    flipped_pattern = np.fliplr(pattern)

    for n in range(4):
        mappings[np.rot90(pattern, n).tobytes()] = outcome
        mappings[np.rot90(flipped_pattern, n).tobytes()] = outcome

print(solve(5))
print(solve(18))

# 203
# 3342470
