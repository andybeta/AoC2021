import sys
import re
import math
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


# Proper positions
# abcdefg
# 1111110 = 0
# 0110000 = 1
# 1101101 = 2
# 1111001 = 3
# 0110011 = 4
# 1011011 = 5
# 1011111 = 6
# 1110000 = 7
# 1111111 = 8
# 1111011 = 9
numbers=[0b1111110,0b0110000,0b1101101,0b1111001,0b0110011,0b1011011,0b1011111,0b1110000,0b1111111,0b1111011]


# be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
#[[['be', 'cfbegad', 'cbdgef', 'fgaecd', 'cgeb', 'fdcge', 'agebfd', 'fecdb', 'fabcd', 'edb'], ['fdgacbe', 'cefdb', 'cefbgd', 'gcbe']]]
def bin_convert(pre_num):
    answer=""
    for letter in ('a','b','c','d','e','f','g'):
        if letter in pre_num:
            answer += "1"
        else:
            answer += "0"
    return answer


def str_to_bin(text):
    answer=0
    for char in text:
        answer = answer<<1
        if char == "1":
            answer += 1
    return answer

total = 0

for pre,post in lines:
    scramble=[0]*10
    bin_scramble=["0b"]*10
    for entry in pre:
        if len(entry) == 2:
            scramble[1]=entry
            bin_scramble[1]=bin_convert(entry)
        if len(entry) == 3:
            scramble[7]=entry
            bin_scramble[7]=bin_convert(entry)
        if len(entry) == 4:
            scramble[4]=entry
            bin_scramble[4]=bin_convert(entry)
        if len(entry) == 7:
            scramble[8]=entry
            bin_scramble[8]=bin_convert(entry)


    a_pos = str_to_bin(bin_scramble[1])^str_to_bin(bin_scramble[7])
    for num in range(10):
        remains = (str_to_bin(bin_convert(pre[num]))^str_to_bin(bin_scramble[4]))^a_pos
        if math.log(remains)/math.log(2) == int(math.log(remains)/math.log(2)) and remains != a_pos:
            d_pos = remains
            break
    d_pos = remains
    nine = str_to_bin(bin_scramble[4])|(a_pos)|(d_pos)
    e_pos = str_to_bin(bin_scramble[8])^nine
    for num in range(10):
        remains = (str_to_bin(bin_convert(pre[num])))|str_to_bin(bin_scramble[1])
        if remains == nine and str_to_bin(bin_convert(pre[num])) != nine:
            five = str_to_bin(bin_convert(pre[num]))
            break
    six = five|e_pos
    b_pos = six^str_to_bin(bin_scramble[8])
    c_pos = b_pos^str_to_bin(bin_scramble[1])
    for num in range(10):
        remains = (str_to_bin(bin_convert(pre[num])))^str_to_bin(bin_scramble[7])^d_pos
        if math.log(remains)/math.log(2) == int(math.log(remains)/math.log(2)) and remains != d_pos:
            g_pos = remains
            break
    zero = str_to_bin(bin_scramble[8])^(g_pos)
    f_pos = str_to_bin(bin_scramble[8])^a_pos^b_pos^c_pos^d_pos^e_pos^g_pos
    two = str_to_bin(bin_scramble[8])^f_pos^c_pos
    three = str_to_bin(bin_scramble[8])^f_pos^e_pos


    scramble[0] = zero
    scramble[2] = two
    scramble[3] = three
    scramble[5] = five
    scramble[6] = six
    scramble[9] = nine

    scramble[1] = str_to_bin(bin_scramble[1])
    scramble[4] = str_to_bin(bin_scramble[4])
    scramble[7] = str_to_bin(bin_scramble[7])
    scramble[8] = str_to_bin(bin_scramble[8])

    post_total=0
    col=1000
    for entry in post:
        num=str_to_bin(bin_convert(entry))
        for i in range(10):
            if scramble[i] == num:
                post_total += (i*col)
                col = col/10
    total += post_total


print(total)

