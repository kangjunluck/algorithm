import sys

input = sys.stdin.readline

n = int(input())
before = 0
dp = [0 for _ in range(n)]
for i in range(n):
    m = int(input())
    if i == 0:
        dp[0] = m
        continue
    elif i == 1:
        dp[1] = dp[0] + m
    else:
        str1 = m + dp[i-2]
        str2 = m + before
        if i - 3 >= 0:
            str2 += max(dp[:i-2])
        dp[i] = max(str1, str2)
    before = m
print(max(dp))



