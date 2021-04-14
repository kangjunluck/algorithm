import sys

input =sys.stdin.readline

n = int(input())
T = [0 for _ in range(n+1)]
P = [0 for _ in range(n+1)]
for i in range(1, n+1):
    a, b = map(int,input().split())
    T[i] = a
    P[i] = b
dp = [0 for _ in range(n+1)]
dp.append(0)
for i in range(n,-1,-1):
    if T[i] > n-i+1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(P[i]+dp[T[i]+i], dp[i+1])
print(dp[1])

