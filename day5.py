import sys
import re
from pprint import pprint

path = sys.argv[1]

read = []
with open(path, 'r') as file:
    read = file.read().splitlines()

lines = []
for line in read:
    row=line.split(" -> ")
    lines.append(row)

xmax = 0
ymax = 0
coords = []
for line in lines:
    starts=[]
    ends=[]
    row=[]
    start=line[0]
    end=line[1]
    xstart,ystart=start.split(",")
    xend,yend=end.split(",")

    if xmax < int(max(xstart,xend)):
        xmax =  int(max(xstart,xend))
    if ymax < int(max(ystart,yend)):
        ymax = int(max(ystart,yend))

    starts.append(int(xstart))
    starts.append(int(ystart))
    starts.append(int(xend))
    starts.append(int(yend))

    row.append(starts)
    coords.append(row)

grid = [[0 for i in range(xmax+1)] for j in range(ymax+1)]
grid2 = [[0 for i in range(xmax+1)] for j in range(ymax+1)]

p1_count=0
p2_count=0
for row in coords:
    for xstart,ystart,xend,yend in row:

        if xstart == xend:
            for y in range(min(ystart,yend),max(ystart,yend)+1):
                grid[y][xstart] += 1
                grid2[y][xstart] += 1
                if grid[y][xstart] == 2:
                    p1_count += 1
                if grid2[y][xstart] == 2:
                    p2_count += 1
        if ystart == yend:
            for x in range(min(xstart,xend),max(xstart,xend)+1):
                grid[ystart][x] += 1
                grid2[ystart][x] += 1
                if grid[ystart][x] == 2:
                    p1_count += 1
                if grid2[ystart][x] == 2:
                    p2_count += 1
        if ystart != yend and xstart != xend:
            xindex=yindex=1
            if xend < xstart:
                xindex = -1
            if yend < ystart:
                yindex = -1
            for x,y in zip(range(xstart,xend+xindex,xindex), range(ystart,yend+yindex,yindex)):
                grid2[y][x] += 1
                if grid2[y][x] == 2:
                    p2_count += 1

print("p1 Count:",p1_count)
print("p2 Count:",p2_count)
