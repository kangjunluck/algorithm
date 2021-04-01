import sys

input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1 ,-1]
INF = sys.maxsize
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    board = [[0 for _ in range(w)] for _ in range(h) ]
    n = int(input())
    for _ in range(n):
        a, b = map(int,input().split())
        board[b][a] = -1
    m = int(input())
    for __ in range(m):
        x1, y1, x2, y2, k = map(int,input().split())
        board[y1][x1] = (y2, x2, k)
    
    ans = [[INF for _ in range(w)] for _ in range(h)]
    ans[0][0] = 0
    q = [(0 ,0, 0)]
    result = 0
    while q:
        x, y, t = q.pop(0)
        if x==h-1 and y ==w-1:
            result = t
            break
        if type(board[x][y]) == type((1, 3)):
            nextR, nextC, t2 = board[x][y]
            if ans[nextR][nextC] > ans[x][y] + t2:
                ans[nextR][nextC] == ans[x][y] + t2
                q.append((nextR,nextC, ans[x][y] + t2))
        else:
            for ar in range(4):
                nextR = x + dr[ar]
                nextC = y + dc[ar]
                if 0<=nextR<h and 0<=nextC<w and board[nextR][nextC] != -1:
                    if ans[nextR][nextC] > 1 + t:
                        ans[nextR][nextC] = 1 + t
                        q.append((nextR, nextC, 1+t))
    if ans[h-1][w-1] == INF:
        print('Impossible')
    else:
        print(ans[h-1][w-1])

