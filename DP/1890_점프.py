# 왜 q로 하면 안될까?

import sys

input = sys.stdin.readline

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        nextR = i + board[i][j]
        nextC = j + board[i][j]
        if 0<=nextR<n:
            dp[nextR][j] += dp[i][j]
        if 0<=nextC<n:
            dp[i][nextC] += dp[i][j]        
print(dp[-1][-1])





