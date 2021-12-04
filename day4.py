import sys
import re

path = sys.argv[1]

with open(path, 'r') as file:
    numbers = file.readline() #load the callers numbers
    lines = file.read().splitlines()
    lines = list(line for line in lines if line) #load everything else as rows

row = list(re.split(' +',lines[0])) # split on spaces
size = len(row) # determine the size of the bingo board (assume square)
numboards = 0
board=[] # an individual board
boards=[] # the list of all boards

def check_num(board,num): # check a board for the called number
    for i,row in enumerate(board):
        #y = [0 if x==1 else x for x in y]
        row = ["X" if x == num else x for x in row] # replace with X if found
        board[i] = row



def check_bingo(board): # checks a board for a bingo
    for row in board:
        res=all(numbers == "X" for numbers in row) # if a row is all Xs then return true
        if res:
            return res

    board_rot = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))] # rotate the board 90deg
    for row in board_rot:
        res=all(numbers == "X" for numbers in row) # if a row (was col) is all Xs then return true
        if res:
            return res
    return res

def sum_board(board): # total all remaining numbers on the board
    total = 0
    for row in board:
        for num in row:
            if num != "X":
                total += int(num)
    return total


i=0
for line in lines: # Load the data into the boards
    row = list(re.split(' +',line.strip()))
    board.append(row)
    if i == size-1: # hacky, should be variable
        boards.append(board)
        numboards += 1
        board=[]
        i=0
    else:
        i += 1

allboards=len(boards) # number of boards
won=0 # has there been a winning board?

for num in numbers.split(","): # for each number
    newboards=boards # copy the list of boards
    for board in newboards: # for each board in the list
        check_num(board,num) # check it for the number
    for board in newboards:
        bingo = check_bingo(board) # check if it's a bingo
        if bingo:                   # if it is then
            total=sum_board(board) # find the total of numbers remaining
            boards.remove(board)    # remove the winning board from the list
            allboards=len(boards) # calculate the number of remaining boards
            if won==0: # if this is the first winning board (ie part 1)
                print("First: ",int(num)*int(total)) # print the total * callers number
                won=1 # set the won flag
            if allboards == 0: # if this is the last remaining board
                print("Last: ",int(num)*int(total))
                exit(0)
