import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

q=[]
for i in range(n):
    for j in range(m):
        if board[i][j] != 0:
            q.append((i, j))
# 빙산 줄이기
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def melt(q):
    info = []
    for dot in q:
        cnt = 0
        for ar in range(4):
            nextR = dot[0] + dr[ar]
            nextC = dot[1] + dc[ar]
            if 0<= nextR < n and 0<= nextC <m and board[nextR][nextC] ==0:
                cnt += 1
        high = board[dot[0]][dot[1]] - cnt
        info.append((dot[0], dot[1], high))
    next = []
    for do in info:
        if do[2] <= 0:
            board[do[0]][do[1]] = 0
        else:
            board[do[0]][do[1]] = do[2]
            next.append((do[0], do[1]))
    return next

# 빙산 갯수 세기
def findland(q):
    visited = [[ 0 for __ in range(m) ] for __ in range(n)]
    num = 0
    for point in q:
        if visited[point[0]][point[1]]: continue
        visited[point[0]][point[1]] = 1
        p = [point]
        num += 1
        while p:
            now = p.pop(0)
            for arr in range(4):
                nextR = now[0] + dr[arr]
                nextC = now[1] + dc[arr]
                if 0 <= nextR < n and 0 <= nextC < m and visited[nextR][nextC] == 0 and board[nextR][nextC] != 0:
                    visited[nextR][nextC] = 1
                    p.append((nextR, nextC))
    return num
ans = 0
while True:
    if findland(q) == 0:
        ans = 0
        break
    elif findland(q) >=2:
        break
    q = melt(q)
    ans += 1 

print(ans) 