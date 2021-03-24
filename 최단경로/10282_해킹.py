import sys
import heapq

input = sys.stdin.readline

T = int(input())

INF = sys.maxsize

for tc in range(1,T+1):
    n, d, c = map(int,input().split())
    board = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int,input().split())
        board[b].append((a, s))
    q= []
    heapq.heappush(q, (0, c))
    ans = [INF for _ in range(n+1)]
    ans[c] = 0
    while q:
        time, now = heapq.heappop(q)
        for next, t in board[now]:
            sumt = t + time
            if sumt < ans[next]:
                ans[next] = sumt
                heapq.heappush(q, (sumt, next))
    cnt = 0
    result = 0
    for step in ans:
        if step != INF:
            cnt += 1
            if step > result:
                result = step
    print(cnt, result)