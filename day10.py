import sys
from collections import deque

path = sys.argv[1]

with open(path, 'r') as file:
    nav = file.read().splitlines()

match_d = { "<" : ">",
            "{" : "}",
            "(" : ")",
            "[" : "]"}

score_d = { ")" : 3,
            "]": 57,
            "}": 1197,
            ">": 25137}

complete_d = { "(" : 1,
            "[": 2,
            "{": 3,
            "<": 4}

score=0
last_open=[]
incomplete=[]
complete_scores=[]
for line in nav:
    corrupt = 0
    last_open=[]
    for char in line:
        # get char
        # if open, set to last_open
        # if close, does it match last_open?
        # if yes, last_open = ""
        # if no, score it and exit
        if char in "[{(<":
            last_open.append(char)
        else:  # it's a closer
            last = last_open[len(last_open)-1]
            if char != match_d[last]:
                # corrupted
                score += score_d[char]
                corrupt = 1
                break
            else:
                last_open = last_open[:-1]
    if corrupt == 0:
        incomplete.append(line)
        last_open.reverse()
        complete_score = 0

        for char in last_open:
            complete_score = complete_score * 5
            complete_score += complete_d[char]
        complete_scores.append(complete_score)

print(score)
complete_scores.sort()
print(complete_scores[int((len(complete_scores)/2))])


