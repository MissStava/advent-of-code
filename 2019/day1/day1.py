import math

file = open("input", "r")

masses = [int(x.strip('\n)')) for x in file.readlines()]

def calculate_fuel(mass):
    fuel = math.floor(mass/3)-2
    if fuel <= 0:
        return 0
    return calculate_fuel(fuel) + fuel


total_fuel = 0
for mass in masses:
    total_fuel += calculate_fuel(mass)

print int(total_fuel)


# Day 1 - 3373568

 # 5057371
