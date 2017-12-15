aFactor = 16807
bFactor = 48271

divider = 2147483647

# aResult = 873
# bResult = 583

# count = 0
# for n in range(40000000):
#     aResult = (aResult * aFactor) % divider
#     bResult = (bResult * bFactor) % divider
#
#     if bin(aResult)[2:].zfill(32)[16:] == bin(bResult)[2:].zfill(32)[16:]:
#         count += 1
#
# print count

count = 0
aList = []
bList = []
aResult = 873
bResult = 583

while True:

    if len(aList) < 5000000:
        aResult = (aResult * aFactor) % divider
        if aResult % 4 == 0:
            aList.append(aResult)

    if len(bList) < 5000000:
        bResult = (bResult * bFactor) % divider
        if bResult % 8 == 0:
            bList.append(bResult)

    if len(aList) == 5000000 and len(bList) == 5000000:
        break

# print len(aList)
# print len(bList)

for n in range(len(bList)):
    if bin(aList[n])[2:].zfill(32)[16:] == bin(bList[n])[2:].zfill(32)[16:]:
        count += 1

print count
