#그냥 싹다 규칙없이 전체를 다 돌아봐야하나?
# 두 동전이 서로 영향을 끼치진 않는다
# 각 동전의 위치를 기억해두고 4방탐색을 해보자
# 왠지 이차 행렬 visited를 써야할 것 같은데.. 두 동전의 visited가 필요하다
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(n)]
visited = [[[[0]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

start = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 'o':
            start.append((i, j))

coin1 = start[0]
coin2 = start[1]

visited[coin1[0]][coin1[1]][coin2[0]][coin2[1]] = 1

q = deque()
q.append((coin1[0], coin1[1], coin2[0], coin2[1], 2, 0))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = -1
while q:
    x1, y1, x2, y2, left, cnt = q.popleft()
    if cnt > 10:
        break
    if left == 1:
        answer = cnt
        break
    if left == 0:
        continue
    for ar in range(4):
        nx1 = x1 + dx[ar]
        ny1 = y1 + dy[ar]

        nx2 = x2 + dx[ar]
        ny2 = y2 + dy[ar]
        # 경우의 수 처리가 중요한듯
        drop = 0
        if nx1<0 or n<=nx1 or ny1<0 or m<=ny1:
            drop += 1
        if nx2<0 or n<=nx2 or ny2<0 or m<=ny2:
            drop += 1
        
        if drop == 2:
            q.append((0, 0, 0, 0, 0, 0))
        elif drop == 1:
            q.append((0, 0, 0, 0, 1, cnt+1))
        else:
            if board[nx1][ny1] == '#':
                nx1 = x1
                ny1 = y1
            if board[nx2][ny2] == '#':
                nx2 = x2
                ny2 = y2
            if visited[nx1][ny1][nx2][ny2] == 0:
                visited[nx1][ny1][nx2][ny2] = 1
                board[x1][y1], board[nx1][ny1] = board[nx1][ny1], board[x1][y1]
                board[x2][y2], board[nx2][ny2] = board[nx2][ny2], board[x2][y2]
                q.append((nx1, ny1, nx2, ny2, 2, cnt+1))
print(answer)
            
