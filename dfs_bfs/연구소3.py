from collections import deque

n, m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

virus = []
cnt = n*n
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            board[i][j] = 0
            cnt -= 1
            virus.append((i, j))
        elif board[i][j] == 0:
            board[i][j] = -1
        elif board[i][j] == 1:
            cnt -= 1
            board[i][j] = '-'
# m 개를 선택해서 bfs를 돌리자
virus_num = len(virus)
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
answer = 1000000
def combi(idx, start):
    global answer
    global cnt
    if idx == m:
        q = deque()
        visited = [[-1]*n for _ in range(n)]
        for ele in sel:
            a, b = virus[ele]
            board[a][b] = 3
            visited[a][b] = 0
            q.append((a, b))
        vir = 0
        while q:
            nowa, nowb = q.popleft()
            
            for ar in range(4):
                nexta = nowa + dr[ar]
                nextb = nowb + dc[ar]
                if 0<=nexta<n and 0<=nextb<n and (board[nexta][nextb] == -1 or board[nexta][nextb] == 0 ) and visited[nexta][nextb] == -1:
                    visited[nexta][nextb] = visited[nowa][nowb] + 1
                    if board[nexta][nextb] == -1:
                        vir += 1
                    q.append((nexta, nextb))
        if vir == cnt:
               
            if board[nowa][nowb] == 0:
                answer = min(answer, visited[nowa][nowb]-1)
            else:
                answer = min(answer, visited[nowa][nowb])   
              

        for ele in sel:
            a, b = virus[ele]
            board[a][b] = 2
        return
    for k in range(start, virus_num):
        sel.append(k)
        combi(idx+1, k+1)
        sel.pop()

sel = []
combi(0, 0)
if answer == 1000000:
    print(-1)
else:
    print(answer)