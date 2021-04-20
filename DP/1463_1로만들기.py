n = int(input())

dp = [0 for _ in range(1000001)]
dp[2] = 1
dp[3] = 1
if n <=3:
    pass
else:
    i = 4
    while i <= n:
        if i%2 == 0 and i%3 == 0:
            dp[i] = min(dp[i//2], dp[i//3], dp[i-1]) + 1
        elif i%2 != 0 and i%3 == 0:
            dp[i] = min(dp[i//3], dp[i-1]) + 1
        elif i%2 == 0 and i%3 != 0:
            dp[i] = min(dp[i//2], dp[i-1]) + 1
        else:
            dp[i] = dp[i-1] + 1
        i += 1

print(dp[n])
