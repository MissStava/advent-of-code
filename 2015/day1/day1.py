file = open("input", "r")

floor = 0
pos = 1
basement = 0
for a in file.read():
    if a == '(':
        floor += 1
    else:
        floor -= 1
    if basement == 0 and floor == -1:
        basement = pos
    pos += 1

print floor # 74 (though results show 73)
print basement # 1795
