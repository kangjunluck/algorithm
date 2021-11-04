import sys
import heapq

input = sys.stdin.readline
INF = 1000000000

def dijkstra(n, x):
    dist = [INF] * (n+1)
    dist[x] = 0
    q = []
    heapq.heappush(q, [0, x])

    while q:
        cost, pos = heapq.heappop(q)
        for p, c in road[pos]:
            c += cost
            if c < dist[p]:
                dist[p] = c
                heapq.heappush(q, [c, p])
    return dist


N, M, X = map(int, input().split())
road = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    road[a].append([b, t])

answer = [0] * (N+1)
for i in range(1, N+1):
    ret = dijkstra(N, i)
    if i == X:
        for idx, r in enumerate(ret):
            answer[idx] += r
    else:
        answer[i] += ret[X]
answer[0] = -1
print(max(answer))