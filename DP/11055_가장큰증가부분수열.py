import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

dp = [0 for _ in range(n)]
dp[n-1] = data[-1]
for i in range(n-2, -1, -1):
    maxi = 0
    for j in range(i+1, n):
        if data[j] > data[i] and maxi <= dp[j]:
            maxi = dp[j]
    if maxi:
        dp[i] = maxi + data[i]
    else:
        dp[i] = data[i]
print(max(dp))