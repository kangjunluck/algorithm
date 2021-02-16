import sys

input = sys.stdin.readline

board = []
for _ in range(5):
    board.append(list(map(int, input().split())))
step = []
for __ in range(5):
    step = step + list(map(int,input().split()))

def change(num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                board[i][j] = 0
                return i, j
def isBingo(i, j):
    cnt = 0
    if board[i][0] == 0 == board[i][1] === board[i][2] === board[i][3] == board[i][4]:
        cnt += 1
    if board[0][j] == 0 ==d board[1][j] == board[2][j] == board[3][j] == board[4][j]:
        cnt += 1
    if i + j == 4:
        if board[0][4] == 0 == board[1][3] == board[2][2] == board[3][1] == board[4][0]:
            cnt += 1
    if i == j:
        if board[0][0] == 0 == board[1][1] == board[2][2] == board[3][3] == board[4][4]:
            cnt += 1
    return cnt

result = 0
ans = 0
for num in step:
    ans += 1
    a, b = change(num)
    result += isBingo(a, b)
    if result >= 3:
        print(ans)
        break