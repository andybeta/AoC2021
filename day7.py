import sys
import math

path = sys.argv[1]

read = []
with open(path, 'r') as file:
    read = file.read().splitlines()

input = read[0].split(",")
crabs = [int(crab) for crab in input]

crabs.sort()

mid = int(math.ceil(len(crabs)/2))
midcrab = crabs[mid]

fuel = 0
for crab in crabs:
    distance = abs(crab-midcrab)
    fuel += distance

print(fuel)


# part 2

least_fuel=0

for crab_pos in range(0,crabs[len(crabs)-1]):
    fuel = 0
    for crab in crabs:
        distance = abs(crab_pos - crab)
        fuel += distance * (distance + 1) / 2

    if (least_fuel > 0 and fuel < least_fuel) or least_fuel == 0:
        least_fuel = fuel

print(least_fuel)
exit(0)
