file = open("input", "r")
presents = [x.strip('\n') for x in file.readlines()]

wrapper = 0
ribbon = 0
for present in presents:
    l, w, h = map(int, present.split('x'))
    wrapper += (2*l*w)+(2*w*h)+(2*h*l)+min([l*w, w*h, h*l])
    ribbon += l+l+w+w+(l*w*h)
print wrapper
# 1586300
print ribbon
# 3753470 too high
