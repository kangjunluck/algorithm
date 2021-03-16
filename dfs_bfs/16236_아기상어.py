import sys

input = sys.stdin.readline

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

q = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            board[i][j] = 0
            start = (i, j, 0)    # 좌표, 시간

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

def isClear():
    global size
    for a in range(n):
        for b in range(n):
            if 0 < board[a][b] < size:
                return False
    return True

size = 2
time = 0
eat = 0
while True:
    if isClear():
        break
    visited = [[0 for _ in range(n)] for _ in range(n)]
    q = []
    q.append(start)
    visited[start[0]][start[1]] = 1
    ans = []
    std = 1000000
    while q:
        now = q.pop(0)
        if std <= now[2]:
            break
        for ar in range(4):
            nextR = now[0] + dr[ar]
            nextC = now[1] + dc[ar]
            if 0<= nextR < n and 0<= nextC < n and visited[nextR][nextC] == 0:
                if 0 < board[nextR][nextC] < size:
                    visited[nextR][nextC] = 1
                    std = ( now[2] + 1 )
                    ans.append((nextR, nextC))
                    break
                elif board[nextR][nextC] == size or board[nextR][nextC] == 0:
                    visited[nextR][nextC] = 1
                    q.append((nextR, nextC, now[2]+1))
                else:
                    continue
    if ans == []:
        break
    ans = sorted(ans, key=lambda x: (x[0], x[1]))
    start = (ans[0][0], ans[0][1], 0)
    board[start[0]][start[1]] = 0
    time += std
    eat += 1
    if eat == size:
        size += 1
        eat = 0
print(time)