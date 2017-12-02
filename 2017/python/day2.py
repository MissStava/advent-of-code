file = open("day2inputs", "r")
lines = file.readlines()

checksum = 0
weightedSum = 0
for line in lines:
    numbers = [int(n.replace('\n', '')) for n in line.split('\t')]
    checksum += max(numbers) - min(numbers)

    for num in numbers:
        for n in range(len(numbers)):
            if num % numbers[n] == 0 and num != numbers[n]:
                weightedSum += num / numbers[n]


print checksum
# Answer = 34925

print weightedSum
# Answer = 221
