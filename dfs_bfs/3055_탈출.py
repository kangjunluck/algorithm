import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(str,input().strip())) for _ in range(n) ]
q =[]
w = []
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 'S':
            q.append((i, j, 0))
            visited[i][j] = 1
        elif board[i][j] == '*':
            w.append((i, j))
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def spread():
    global w
    cnt = len(w)
    while cnt > 0:
        nowW = w.pop(0)
        for arr in range(4):
            nextRw = nowW[0] + dr[arr]
            nextCw = nowW[1] + dc[arr]
            if 0 <= nextRw < n and 0 <= nextCw < m and board[nextRw][nextCw] == '.':
                board[nextRw][nextCw] = '*'
                w.append((nextRw, nextCw))
        cnt -= 1
std = 0
ans = 'KAKTUS'
isGet = False
while q:
    if isGet:
        break
    now = q.pop(0)
    if std == now[2]:
        spread()
        std += 1
    for ar in range(4):
        nextR = now[0] + dr[ar]
        nextC = now[1] + dc[ar]
        if 0<=nextR<n and 0<=nextC<m and visited[nextR][nextC] == 0 and board[nextR][nextC] == 'D':
            ans = now[2] + 1
            isGet = True
            break
        if 0<=nextR<n and 0<=nextC<m and visited[nextR][nextC] == 0 and board[nextR][nextC] == '.':
            visited[nextR][nextC] =1
            q.append((nextR, nextC, now[2]+1))

print(ans)
