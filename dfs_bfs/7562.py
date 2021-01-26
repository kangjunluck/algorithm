# 최소 거리 계산이기 때문에 bfs를 쓸 것 같다. 100 * 100 이라 dfs로 해야할 것 같다. 시간 초과가 난다

import sys
from collections import deque

sys.stdin = open('7562.txt', 'r')
input = sys.stdin.readline

case = int(input())

dr = [1, 1, 2, 2, -1, -1, -2, -2]
dc = [2, -2, 1, -1, 2, -2, 1, -1]

for i in range(case):
    n = int(input())
    a, b = list(map(int, input().split())) # 시작지점
    x, y = list(map(int, input().split())) # 도착지점
    board = [[0 for _ in range(n)] for __ in range(n)]
    if (a,b)==(x,y):
        print(-1)
    else:
        board[a][b] = 1
        board[x][y] = -2
        q = deque()
        q.append((a,b))
        ans = 0
        result=[]
        while q:
            c, r = q.popleft()
            for j in range(8):
                nextC = c + dc[j]
                nextR = r + dr[j]
                if 0<=nextC<n and 0<=nextR<n and board[nextC][nextR] == -2:               
                    ans = board[c][r]
                    result.append(ans)
                if 0<=nextC<n and 0<=nextR<n and board[nextC][nextR] == 0:
                    q.append((nextC, nextR))
                    board[nextC][nextR] = board[c][r] + 1               
        print(min(result))