import sys

path = sys.argv[1]

with open(path, 'r') as file:
    diag = file.read().splitlines()

def get_gamma(diag): # returns the gamma and epsilon for a set of data
    records=len(diag) # number of records in the data
    l=len(diag[0]) # length of one record (assuming they are the same)
    index=2**(l-1) # for bin operations - the last bit value
    trimmer=(2**l)-1 # a mask for trimming 01111111111...etc
    total=[0]*l # array of length 'l' full of zeroes

    # Don't ask
    for line in diag: # for each line in the input data
        num = int(line,2) # convert it to dec
        for i in range(l): # for each bit position
            if num >= index: # if it's higher than index (ie there is a 1 in highest bit)
                total[i] += 1 # inc the counter for that position
            num = num << 1 # left shift the row
            num = num & trimmer # and mask off the leftmost bit
    
    gamma=""
    epsilon=""
    
    for i in range(l): # for each bit
        if total[i] >= records/2: # if the counter is more than half (or equal) ie. 1s in that position
            gamma+="1" # gamma for that position is 1
            epsilon+="0" # and epsilon for that position is 0
        else:
            gamma+="0" # else the opposite is true
            epsilon+="1"
    return(gamma,epsilon)

gamma,epsilon=get_gamma(diag) # So.. get the g & e for our whole data

power=int(gamma,2) * int(epsilon,2) # etc
print("Power:"+str(power))

oxy=diag # initialise oxy and co2 data sets to be the same as our input data
co2=diag
oxy_gamma,oxy_epsilon=get_gamma(oxy) # get initial gamma for each (don't care about epsilon)
co2_gamma,co2_epsilon=get_gamma(co2)


for pos in range(len(gamma)): # for each position 0...len
    oxy_char=oxy_gamma[pos] # find the bit there
    co2_char=co2_gamma[pos]

    if len(oxy) > 1: # check we don't kill the last row of data
        oxy=[row for row in oxy if row[pos] == oxy_char] # include only oxy rows that match the oxy char

    if len(co2) > 1:
        co2=[row for row in co2 if row[pos] != co2_char] # include only co2 rows that don't match the co2 char

    if  len(co2) == 1 and len(oxy) ==1: # if they both only have one element, we're done
        break
    oxy_gamma,oxy_epsilon=get_gamma(oxy) # otherwise find the new gamma for each
    co2_gamma,co2_epsilon=get_gamma(co2)

final_oxy=oxy[0] # set the final values
final_co2=co2[0]

lsr=int(final_oxy,2) * int(final_co2,2) # and multiply them
print("Life Support:"+str(lsr))
