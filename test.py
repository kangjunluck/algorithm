import sys

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]

    start = 0
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt += 1
            if board[i][j] == 2:
                start = (i, j)

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    result = []
    def dfs(i, j, cnt):
        global result
        if cnt == 3:
            return
        for ar in range(4):
            isCan = False
            nr = i + dr[ar]
            nc = j + dc[ar]
            while 0<=nr<n and 0<=nc<n and board[nr][nc] == 0:
                nr += dr[ar]
                nc += dc[ar]
            if 0<=nr<n and 0<=nc<n and  board[nr][nc] == 1:
                isCan = True
                nr += dr[ar]
                nc += dc[ar]
            if isCan:
                while 0<= nr<n and 0<=nc<n:
                    if board[nr][nc] == 0:
                        board[i][j] = 0
                        board[nr][nc] = 2
                        dfs(nr, nc, cnt + 1)
                        board[nr][nc] = 0
                        board[i][j] = 2
                    else:
                        result.append((nr, nc))
                        board[i][j] = 0
                        board[nr][nc] = 2
                        dfs(nr, nc, cnt + 1)
                        board[nr][nc] = 1
                        board[i][j] = 2
                        break
                    nr += dr[ar]
                    nc += dc[ar]

    dfs(start[0], start[1], 0)
    print('#{} {}'.format(tc, len(set(result))))