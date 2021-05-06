import sys

input = sys.stdin.readline

n = int(input())

data = list(map(int,input().split()))
dp = [0 for _ in range(n)]
dp[0] = data[0]

for idx in range(1,n):
    # idx가 홀수 일때
    if idx % 2:
        maxi = 0
        for i in range(idx//2):
            if maxi < dp[i] + dp[idx-1-i]:
                maxi = dp[i] + dp[idx-1-i]
        if maxi < dp[idx//2]*2:
            maxi = dp[idx//2] * 2
        dp[idx] = max(maxi, data[idx])
    # idx가 짝수 일때
    else:
        maxi = 0
        for i in range(idx//2):
            if maxi < dp[i] + dp[idx-1-i]:
                maxi = dp[i] + dp[idx-1-i]
        dp[idx] = max(maxi, data[idx])

print(dp[-1])