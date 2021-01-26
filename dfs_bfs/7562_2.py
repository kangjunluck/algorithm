# dfs로 해보자

import sys

sys.setrecursionlimit(1000000)

sys.stdin = open('7562.txt', 'r')
input = sys.stdin.readline

case = int(input())

dr = [1, 1, 2, 2, -1, -1, -2, -2]
dc = [2, -2, 1, -1, 2, -2, 1, -1]

def dfs(c,r):
    ans = 1
    for k in range(8):
        nextC = c + dc[k]
        nextR = r + dr[k]
        if 0<=nextC<n and 0<=nextR<n and board[nextC][nextR] == -2:             
            return ans
        if 0<=nextC<n and 0<=nextR<n and board[nextC][nextR] == 0:
            board[nextC][nextR] = 1
            ans += dfs(nextC, nextR)           
    return ans

for i in range(case):

    n = int(input())
    a, b = list(map(int, input().split())) # 시작지점
    x, y = list(map(int, input().split())) # 도착지점
    board = [[0 for _ in range(n)] for __ in range(n)]

    if a==x and b==y:
        print(-1)
    else:
        board[a][b] = 1
        board[x][y] = -2
        print(dfs(a, b))