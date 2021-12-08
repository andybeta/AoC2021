import sys
import re
from pprint import pprint

path = sys.argv[1]

counter=[0]*10

read = []
with open(path, 'r') as file:
    read = file.read().splitlines()

lines = []
for line in read:
    pre,post=re.split(" \| ",line)
    pre=re.split(" ",pre)
    post=re.split(" ",post)
    row = [pre,post]
    lines.append(row)

    for number in post:
        if len(number) == 2:
            counter[1] += 1
        if len(number) == 3:
            counter[7] += 1
        if len(number) == 4:
            counter[4] += 1
        if len(number) == 7:
            counter[8] += 1

print(sum(counter))


