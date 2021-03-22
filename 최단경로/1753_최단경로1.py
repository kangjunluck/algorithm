import sys
import heapq

input = sys.stdin.readline

INF = 10000000
n, m = map(int, input().split())
start = int(input())


board = [[] for _ in range(n+1)]
for _ in range(m):
    v, e, k = map(int, input().split())
    board[v].append((e, k)) # 다음점, 거리 표시

ans = [INF for _ in range(n+1)]
ans[start] = 0
q = []
heapq.heappush(q, (0, start)) # 거리와 지점

while q:
    short, now = heapq.heappop(q)  # now[0] 거리, now[1] 노드
    for nextP, l in board[now]:
        if short + l < ans[nextP]:
            ans[nextP] = short + l
            heapq.heappush(q, (short + l, nextP))
for mm in range(1,n+1):
    if ans[mm] == INF:
        print('INF')
    else:
        print(ans[mm])