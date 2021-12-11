# idea: load it all into a big array. For each element, check if its NSEW neighbours are > it. If yes, add 1 and sum for total risk
import sys
from collections import deque

path = sys.argv[1]

with open(path, 'r') as file:
    depths = file.read().splitlines()

def bfs(point):
    queue=deque()
    checked=[]
    size=0
    queue.append((point))

    while len(queue) > 0:
        point=queue.popleft()
        if point in checked:
            continue
        row,col=point
        size += 1
        checked.append(point)
        if row>0:
            north=depths[row-1][col]
            if north < "9":
                queue.append((row-1,col))
        if col>0:
            west=depths[row][col-1]
            if west < "9":
                queue.append((row,col-1))
        if row<len(depths)-1:
            south=depths[row+1][col]
            if south < "9":
                queue.append((row+1,col))
        if col<len(depths[row])-1:
            east=depths[row][col+1]
            if east < "9":
                queue.append((row,col+1))
    

    return size


total=0
basinsizes=[]
for row in range(len(depths)):
    for col in range(len(depths[row])):
        target=depths[row][col]
        if row>0:
            north=depths[row-1][col]
            if north <= target:
                continue
        if col>0:
            west=depths[row][col-1]
            if west <= target:
                continue
        if row<len(depths)-1:
            south=depths[row+1][col]
            if south <= target:
                continue
        if col<len(depths[row])-1:
            east=depths[row][col+1]
            if east <= target:
                continue
        #target is low point
        total += 1 + int(target)

        point=(row,col)
        size=bfs(point)
        basinsizes.append(size)

print(total)
a,b,c=sorted(basinsizes,reverse=True)[:3]
print(a*b*c)

