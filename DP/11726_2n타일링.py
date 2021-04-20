n = int(input())

dp = [0 for _ in range(1001)]
dp[1] = 1
dp[2] = 2
if n <=2:
    pass
else:
    i = 3
    while i<=n:
        dp[i] = dp[i-1] + dp[i-2]
        i += 1
print(dp[n]%10007)