import sys
import heapq

n = int(input())
m = int(input())

board = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int,input().split())
    board[a].append((b, c)) # 도착지점, 거리

start, end = map(int, input().split())

q = []
heapq.heappush(q, (start, 0))
INF = sys.maxsize
ans = [INF for _ in range(n+1)]
ans[start] = 0

while q:
    now, short = heapq.heappop(q)
    for next, l in board[now]:
        if short + l < ans[next]:
            ans[next] = short + l
            heapq.heappush(q, (next, short+l))
print(ans[end])