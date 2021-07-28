n, m = map(int,input().split())

# 북동남서, 0 1 2 3
y, x, d = map(int,input().split())
dx = [[-1, 0, 1, 0],[0, -1, 0, 1],[1, 0, -1, 0],[0, 1, 0, -1]]
dy = [[0, 1, 0, -1],[-1, 0, 1, 0],[0, -1, 0, 1],[1, 0, -1, 0]]

bx = [0, -1, 0, 1]
by = [1, 0, -1, 0]

board = [list(map(int,input().split())) for _ in range(n)]

cnt = 0
while True:
    if board[y][x] == 0:
        board[y][x] = 2
        cnt += 1
    isStep1 = False
    for i in range(4):
        nx = x + dx[d][i]
        ny = y + dy[d][i]
        if board[ny][nx] == 0:
            if nx - x >0: d = 1
            elif nx - x <0: d = 3
            if ny - y >0: d =2
            elif ny - y <0: d = 0
            x = nx
            y = ny
            isStep1 = True
            break
    
    if isStep1: continue
    if board[y + by[d]][x + bx[d]] == 1:
        break
    x += bx[d]
    y += by[d]
print(cnt) 

    