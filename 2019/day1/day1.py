file = open("input", "r")

def calculate_fuel(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    return calculate_fuel(fuel) + fuel

print int(sum([calculate_fuel(int(mass)) for mass in file.readlines()]))

# 3373568
# 5057371
