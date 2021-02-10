import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().strip())))
result = []
for i in range(n):
    for j in range(m):
        width = m-1 - j
        height = n-1 - i
        std = min(width, height)
        for k in range(1,std+1):
            if board[i][j] == board[i+k][j] and board[i][j] == board[i+k][j+k] and board[i][j] == board[i][j+k] and k!=0:
                result.append((k+1)**2)
if result:
    print(max(result))
else:
    print(1)

        

