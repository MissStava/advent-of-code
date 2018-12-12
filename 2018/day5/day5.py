file = open("input", "r")

poly = file.read()

def collapse(poly):
  new_poly = ['']
  for letter in poly:
    last_letter = new_poly[-1]
    if last_letter != letter and last_letter.lower() == letter.lower():
      new_poly.pop()
    else:
      new_poly.append(letter)
  return len(new_poly) - 1

print "Day 5 Part 1 = " + str(collapse(poly))

lengths = [collapse(poly.replace(c, '').replace(c.upper(), '')) for c in 'abcdefghijklmnopqrstuvwxyz']

print "Day 5 Part 2 = " + str(min(lengths))
