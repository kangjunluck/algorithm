import sys

input = sys.stdin.readline

n, l, r = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(n)]


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

ans = 0
while True:
    cnt = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]: continue
            cnt += 1
            visited[i][j] = 1
            q = [(i, j)]
            total = board[i][j]
            area = [(i, j)]
            while q:
                now = q.pop(0)
                for ar in range(4):
                    nextR = now[0] + dr[ar]
                    nextC = now[1] + dc[ar]
                    
                    if 0<=nextR<n and 0<=nextC<n and visited[nextR][nextC] == 0:
                        if l <= abs(board[now[0]][now[1]] - board[nextR][nextC]) <= r:
                            visited[nextR][nextC] = 1
                            area.append((nextR, nextC))
                            total += board[nextR][nextC]
                            q.append((nextR,nextC))
            if len(area) > 1:
                divi = total // len(area)
                for k in area:
                    board[k[0]][k[1]] = divi
    if cnt == n**2:
        break
    ans += 1
print(ans)