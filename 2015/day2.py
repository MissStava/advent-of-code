import math

with open('day2.input', 'r') as file:
  data = file.read().splitlines()

def calculate_wrapping_paper(line):
  length, width, height = map(int, line.split('x'))

  lw = length*width
  wh = width*height
  hl = height*length

  return 2*(lw + wh + hl) + min(lw, wh, hl)

def calculate_ribbon(line):
  dimensions = sorted(map(int, line.split('x')))

  return 2*dimensions[0] + 2*dimensions[1] + math.prod(dimensions)

wrapping_paper = sum([calculate_wrapping_paper(line) for line in data])
print("Part 1 answer = {}".format(wrapping_paper))

ribbon = sum([calculate_ribbon(line) for line in data])
print("Part 2 answer = {}".format(ribbon))