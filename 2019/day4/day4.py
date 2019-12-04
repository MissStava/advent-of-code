
tot = 0
part2_tot = 0
for m in xrange(402328,864247):
    n = str(m)

    doubles = 0
    solo_double = 0
    not_decrease = 0
    for x in range(5):
        if n[x] == n[x+1]:
            doubles += 1
            if n.count(n[x]) == 2:
                solo_double += 1

        if int(n[x+1]) < int(n[x]):
            not_decrease += 1

    if doubles >= 1 and not_decrease == 0 and solo_double == 1:
        tot += 1
        # print m
# print tot

    if not any(c1 > c2 for c1, c2 in zip(str(m), str(m)[1:])) and any(c1 == c2 for c1, c2 in zip(str(m), str(m)[1:])) and any(c for c in str(m) if str(m).count(c) == 2):
        part2_tot += 1
print part2_tot

#454
