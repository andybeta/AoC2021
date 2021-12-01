# open input file day1.txt with 'r' read permissions, and load the values into 'depths'
with open('day1.txt', 'r') as file:
    depths = [line.strip() for line in file]

# part 1

#initialise some counters / totals
deeper=0 # this is a counter for when it gets deeper
prev_depth=0 # this is the previous depth value (so I can compare)

for depth in depths: # for each value in turn in depths
    depth=int(depth) # make it an integer (so i can do maths with it)
    if depth > prev_depth: # if it's deeper (higher value) than the previous depth then...
        deeper += 1 # increment deeper counter
    prev_depth=depth # set the previous depth to this current one, for the next go round and loop back for the next value

print(deeper-1) # output the result (-1 because the first comparison deosn't count)


# part 2

count=0 # counter for the items in the set
deeper=0 # counter for when a set of 3 values are deeper than the previous 3
last3=0 # value of the last 3 depths
total3=0 # value of the current 3 depths
drop=0 # the value of the depth to 'drop' out of the set

for depth in depths: # for each value in depths
    count += 1 # increase the counter
    depth=int(depth) # make depth an integer (so i can do maths with it)
    total3 = last3 + depth - drop # set total3 = last3 + the new depth - the old depth

    if count < 3: # If we're in the first three values then
        last3 = total3 # set last3 to total3 
        continue # and skip to the next depth value in the set (ignore the rest of this loop)

    if total3 > last3: # if the new total is deeper (higher value) than the last 3 depths then
        deeper += 1 # increase the total count

    last3 = total3 # set the last3 to the current value
    drop = int(depths[count-3]) # set drop to the value 'leaving' the current set of 3 (and loop back to the start)

print(deeper-1) # output the results (-1 because the first comparison doesn't count)
