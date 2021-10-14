from collections import deque

n, m = map(int, input().split())
board = [list(map(str,input().strip())) for _ in range(n)]

red = 0
blu = 0
hol = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            board[i][j] ='.'
            red = (i, j)
        elif board[i][j] == 'B':
            board[i][j] ='.'
            blu = (i, j)
        elif board[i][j] == 'O':
            hol = (i, j)

q = deque()
q.append((red[0], red[1], blu[0], blu[1], 0))

visited = [[[[0]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
visited[red[0]][red[1]][blu[0]][blu[1]] = 1
dr = [1, -1, 0, 0] # 하 상 우 좌
dc = [0, 0, 1, -1]
isAnswer = False
answer = -1
while q:
    now = q.popleft()
    Rr, Rc, Br, Bc, cnt = now
    if cnt == 10:
        break
    for ar in range(4):
        drop = 0
        nRr = Rr + dr[ar]
        nRc = Rc + dc[ar]
        nBr = Br + dr[ar]
        nBc = Bc + dc[ar]
        while board[nRr][nRc] == '.':
            nRr += dr[ar]
            nRc += dc[ar]
        if board[nRr][nRc] == 'O':
            drop = 1
        nRr -= dr[ar]
        nRc -= dc[ar]
        while board[nBr][nBc] == '.':
            nBr += dr[ar]
            nBc += dc[ar]
        if board[nBr][nBc] == 'O':
            drop = -1
        nBr -= dr[ar]
        nBc -= dc[ar]
        if drop == 1:
            isAnswer = True
            answer = cnt + 1
            break
        if drop == -1:
            continue
        
        if nRr == nBr and nRc == nBc:
            if ar == 0:
                if Rr < Br:
                    nRr -= dr[ar]
                else:
                    nBr -= dr[ar]
            elif ar == 1:
                if Rr > Br:
                    nRr -= dr[ar]
                else:
                    nBr -= dr[ar]
            elif ar == 2:
                if Rc < Bc:
                    nRc -= dc[ar]
                else:
                    nBc -= dc[ar]
            else:
                if Rc > Bc:
                    nRc -= dc[ar]
                else:
                    nBc -= dc[ar]
        if visited[nRr][nRc][nBr][nBc] == 1:continue
        visited[nRr][nRc][nBr][nBc] == 1
        q.append((nRr, nRc, nBr, nBc, cnt + 1))

    if isAnswer:
        break
            
print(answer)

