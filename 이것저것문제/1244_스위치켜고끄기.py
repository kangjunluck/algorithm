import sys

input = sys.stdin.readline

bulb = int(input())
board = list(map(int,input().split()))
n = int(input())

def change(index):
    if board[index] == 1: board[index] = 0
    else: board[index] = 1

def mando(gender, getnum, board, bulb):
    if gender == 1:
        for i in range(getnum, bulb+1, getnum):
            change(i-1)
        return board
    else:
        index = getnum-1
        change(index)
        len = 1
        while True:         
            if 0 > index-len or index+len >= bulb:
                break
            else:
                if board[index-len] == board[index+len]:
                    change(index-len)
                    change(index+len)
                else:
                    break
            len += 1
        return board



for step in range(n):
    gender, getnum = map(int,input().split())
    mando(gender, getnum, board, bulb)
for k in range(1, bulb+1):
    print(board[k-1], end=' ')
    if k%20 == 0:
        print()