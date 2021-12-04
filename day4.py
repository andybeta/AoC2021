import sys
import re

path = sys.argv[1]

with open(path, 'r') as file:
    numbers = file.readline()
    lines = file.read().splitlines()
    lines = list(line for line in lines if line)

row = list(re.split(' +',lines[0]))
size = len(row)
numboards = 0
board=[]
boards=[]

def check_num(board,num):
    for i,row in enumerate(board):
        #y = [0 if x==1 else x for x in y]
        row = ["X" if x == num else x for x in row]
        board[i] = row



def check_bingo(board):
    for row in board:
        res=all(numbers == "X" for numbers in row) 
        if res:
            return res

    board_rot = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
    for row in board_rot:
        res=all(numbers == "X" for numbers in row) 
        if res:
            return res
    return res
    
def sum_board(board):
    total = 0
    for row in board:
        for num in row:
            if num != "X":
                total += int(num)
    return total


i=0
for line in lines:
    row = list(re.split(' +',line.strip()))
    board.append(row)
    if i == 4:
        boards.append(board)
        numboards += 1
        board=[]
        i=0
    else:
        i += 1

allboards=len(boards)
won=0

for num in numbers.split(","):
    for board in boards:
        check_num(board,num)
        bingo = check_bingo(board)
        if bingo:
            total=sum_board(board)
            boards.remove(board)
            allboards=len(boards)
            if won==0:
                print("First: ",int(num)*int(total))
                won=1
            if allboards == 1:
                print("Last: ",int(num)*int(total))
                exit(0)
