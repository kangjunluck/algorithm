import sys
import heapq

INF = sys.maxsize

T = int(input())

for tc in range(1,T+1):
    n, m = map(int,input().split())
    data = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, t = map(int,input().split())
        data[a].append((b, t))
        data[b].append((a, t))
    print(data)
    q = []
    heapq.heappush(q, (0, 1))
    ans = [INF for _ in range(n+1)]
    ans[1] = 0
    while q:
        print(ans)
        short, now = heapq.heappop(q)
        for next, time in data[now]:
            if time < ans[next]:
                ans[next] = time
                heapq.heappush(q, (time, next))
    print(ans)
    result = 0
    for a in ans:
        if a != INF:
            result += a
    print('#{} {}'.format(tc, result))

