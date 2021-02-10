import sys

input = sys.stdin.readline

n = int(input())
info = list(map(int,input().split()))
board = [10]*n
cnt = 0
for num in info:
    cnt += 1
    if cnt == 1:
        board[num] = cnt
    else:
        for i in range(n):
            if i == 0:
                if num == 0 and board[0] == 10:
                    board[i] = cnt
                    break
            else:
                if board[i] == 10:
                    same = 0
                    for j in range(i):
                        if cnt < board[j]:
                            same += 1
                    if same == num:
                        board[i] = cnt
                        break

for step in board:
    print('{}'.format(step), end=' ')



