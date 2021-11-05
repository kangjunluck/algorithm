import sys
import heapq

input = sys.stdin.readline

INF = sys.maxsize

def dijk(s, e):
    dis = [INF] * (n+1)
    dis[s] = 0
    q = []
    heapq.heappush(q, (0, s))
    while q:
        weight, next = heapq.heappop(q)
        for w, v in data[next]:
            if dis[v] > weight + w:
                dis[v] = weight + w
                heapq.heappush(q, (dis[v], v))
    return dis[e]

n, m = map(int, input().split())
data = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int,input().split())
    data[a].append((c, b))
    data[b].append((c, a))

s1, s2 = map(int, input().split())

case1 = dijk(1, s1) + dijk(s1, s2) + dijk(s2, n)
case2 = dijk(1, s2) + dijk(s2, s1) + dijk(s1, n)

## 요부분이 애매합니다잉 > 블로그 참고..
if case1 >= INF and case2 >= INF:
    print(-1)
else:
    print(min(case1, case2))

