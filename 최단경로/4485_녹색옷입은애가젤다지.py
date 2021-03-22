import sys
import heapq

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
INF = sys.maxsize
tc = 1
while True:
    n = int(input())
    if n == 0:
        break
    board = [list(map(int, input().split())) for _ in range(n)]
    q = []
    heapq.heappush(q, (board[0][0], 0, 0)) # 잃은 돈, 좌표
    ans = [[INF for _ in range(n)] for _ in range(n)]
    ans[0][0] = board[0][0]
    result = 0
    while q:
        money, a, b = heapq.heappop(q)
        if a == n-1 and b == n-1:
            result = money
        for ar in range(4):
            nr = a + dr[ar]
            nc = b + dc[ar]
            if 0<= nr < n and 0<= nc < n:
                if money + board[nc][nr] < ans[nr][nc]:
                    ans[nr][nc] = money + board[nc][nr]
                    heapq.heappush(q, (money + board[nr][nc], nr, nc))
    print('Problem {}: {}'.format(tc, result))
    tc += 1