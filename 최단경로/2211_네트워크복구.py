import sys
import heapq

input = sys.stdin.readline

n, m = map(int,input().split())

INF = sys.maxsize
board = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int,input().split())
    board[a].append((b, c))
    board[b].append((a, c))
times = [INF for _ in range(n+1)]
times[1] = 0
ans = [0 for _ in range(n+1)]
q=[]
heapq.heappush(q, (0, 1))
while q:
    short, now = heapq.heappop(q)
    for next, time in board[now]:
        sumtime = time + short
        if sumtime < times[next]:
            times[next] = sumtime
            ans[next] = now
            heapq.heappush(q, (sumtime, next))
cnt = 0
result = []
for step in ans:
    if step !=0:
        cnt += 1
print(cnt)
for x in range(n+1):
    if ans[x] !=0:
        print(x, ans[x])
