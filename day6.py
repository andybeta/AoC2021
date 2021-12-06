import sys

path = sys.argv[1]

read = []
with open(path, 'r') as file:
    read = file.read().splitlines()

fishes = read[0].split(",")
fishes = [int(fish) for fish in fishes]

fishcount = [0]*9

# load fishcount
for fish in fishes:
    fishcount[fish] += 1

print(fishcount)

days = 256

for day in range(days):
    new_fishcount = fishcount
    new_fish = fishcount[0]
    for fish in range(9):
        today_fish = fishcount[fish]
        if fish == 0 and fishcount[0] > 0:
            new_fishcount[0] = 0 # deal with the new ones at the end
        elif fish > 0:
            new_fishcount[fish] = 0
            new_fishcount[fish-1] = today_fish
    if new_fish > 0:
        new_fishcount[6] += new_fish
        new_fishcount[8] = new_fish
    fishcount = new_fishcount
    if day == 80:
        print(sum(fishcount))

print(sum(fishcount))
