import sys
import heapq
import copy

input = sys.stdin.readline

n, m = map(int, input().split())
INF = sys.maxsize
board = [[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int ,input().split())
    board[a][b] = t
    board[b][a] = t

info = []
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            board[i][j] = 0
        if board[i][j] != 0 and board[i][j] != INF and i < j:
            info.append((i, j))

# 일단 검문이 없을때 만들어 보자.
ans = [INF for _ in range(n+1)]
ans[1] = 0
q=[]
heapq.heappush(q, (0, 1)) # 거리, 시작 노드
while q:
    short, now = heapq.heappop(q)
    if now == n:
        break
    for next in range(1, n+1):
        time = board[now][next]
        if time == INF or time == 0: continue
        sumtime = time + short
        if sumtime < ans[next]:
            ans[next] = sumtime
            heapq.heappush(q, (sumtime, next))
normal = ans[n]

maxi = 0
for step in info:
    coboard = copy.deepcopy(board)
    x, y = step[0], step[1]
    coboard[x][y] = INF
    coboard[y][x] = INF
    ans = [INF for _ in range(n+1)]
    ans[1] = 0
    q=[]
    heapq.heappush(q, (0, 1)) # 거리, 시작 노드
    while q:
        short, now = heapq.heappop(q)
        if now == n:
            break
        for next in range(1, n+1):
            time = coboard[now][next]
            if time == INF or time == 0: continue
            sumtime = time + short
            if sumtime < ans[next]:
                ans[next] = sumtime
                heapq.heappush(q, (sumtime, next))
    part = ans[n]
    if maxi < part:
        maxi = part
ans = maxi - part
if ans > 0:
    print(ans)
else:
    print(-1)
