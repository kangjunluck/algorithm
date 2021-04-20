import sys

input = sys.stdin.readline


T = int(input())

dp = [0 for _ in range(11)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
i = 4

for tc in range(1,T+1):
    n = int(input())
    if dp[n]:
        print(dp[n])
        continue
    while i <= n:
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        i += 1
    print(dp[n])