import sys
from collections import deque

path = sys.argv[1]

with open(path, 'r') as file:
    data = file.read().splitlines()

flash=0
dumbos=[]
checked=[]
to_check=deque()

for row in data:
    dumbo_row=[]
    for item in row:
        dumbo_row.append(int(item))
    dumbos.append(dumbo_row)


def bfs(to_check):
    global flash
    while len(to_check) > 0:
        point=to_check.popleft()
        row,col = point
        for i in range(-1,2):
            for j in range(-1,2):
                if i == 0 and j == 0:
                    continue
                if i == -1 and row == 0:
                    continue
                if j == -1 and col == 0:
                    continue
                if i == +1 and row == 9:
                    continue
                if j == +1 and col == 9:
                    continue
                new_point = (row+i,col+j)
                if dumbos[row+i][col+j] == 0 and new_point in checked:
                    continue
                dumbos[row+i][col+j] += 1
                if dumbos[row+i][col+j] >= 10:
                    checked.append(point)
                    to_check.append(new_point)
                    dumbos[row+i][col+j] = 0
                    flash += 1


count=0
while True:
    count += 1
    checked=[]
    for row in range(10):
        for col in range(10):
            point=(row,col)
            checked.append(point)
            dumbos[row][col] += 1
            if dumbos[row][col] >= 10:
                to_check.append(point)
                dumbos[row][col] = 0
                flash += 1
    bfs(to_check)
    if count == 100:
        print(flash)
    brightness = 0
    for row in range(10):
        brightness += sum(dumbos[row])
    if brightness == 0:
        print(count)
        exit(0)
    
    
