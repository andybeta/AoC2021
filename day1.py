with open('day1.txt', 'r') as file:
    depths = [line.strip() for line in file]

deeper1=0
deeper2=0

for i in range(len(depths)-1):

    if int(depths[i]) < int(depths[i+1]):
        deeper1 += 1

    if i < (len(depths)-3) and int(depths[i]) < int(depths[i+3]):
        deeper2 += 1

print(deeper1)
print(deeper2)
