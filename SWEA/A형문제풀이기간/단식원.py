from collections import deque

T = int(input())

for tc in range(1,T+1):
    n, m = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    answer = 0
    chickens = []
    empty = []
    zeronum = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2: chickens.append((i, j))
            if board[i][j] == 0: 
                empty.append((i, j))
                zeronum += 1
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    for i in range(len(empty)):
        board[empty[i][0]][empty[i][1]] = 1
        for j in range(i+1, len(empty)):
            board[empty[j][0]][empty[j][1]] = 1
            for k in range(j+1, len(empty)):
                board[empty[k][0]][empty[k][1]] = 1
                
                visited = [[0 for _ in range(m)] for _ in range(n)]
                start = zeronum - 3   
                q = deque(chickens)
                while q:
                    na, nb = q.popleft()
                    for ar in range(4):
                        nextR = na + dr[ar]
                        nextC = nb + dc[ar]
                        if 0<= nextR < n and 0<= nextC < m and visited[nextR][nextC] == 0 and board[nextR][nextC] == 0:
                            visited[nextR][nextC] = 1
                            start -= 1
                            q.append((nextR, nextC))
                if answer < start:
                    answer = start

                board[empty[k][0]][empty[k][1]] = 0
            board[empty[j][0]][empty[j][1]] = 0
        board[empty[i][0]][empty[i][1]] = 0

    print('#{} {}'.format(tc, answer))