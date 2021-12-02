import sys
import csv

path = sys.argv[1]

route=[]
with open(path, 'r') as file:
    route = list(csv.reader(file, delimiter=" "))

xpos=zpos=0
depth=0

for vector in route:
    (direction,value)=vector
    if direction == "forward":
        xpos += int(value)
        depth += zpos * int(value)
    if direction == "down":
        zpos += int(value)
    if direction == "up":
        zpos -= int(value)

result=xpos*zpos
result2=xpos*depth
print(result, result2)


