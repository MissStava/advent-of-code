import hashlib

def find_increment(input, final_state):
  increment = 1

  while True:
    encoded_input = (input + str(increment)).encode("utf-8")
    hashed_input = hashlib.md5(encoded_input).hexdigest()

    if hashed_input[:len(final_state)] == final_state:
      break
    
    increment += 1

  return increment

input = "yzbqklnj"

print("Part 1 answer = {}".format(find_increment(input, "00000")))
# 282749

print("Part 2 answer = {}".format(find_increment(input, "000000")))
# 9962624
