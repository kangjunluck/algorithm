import sys

input = sys.stdin.readline

n = int(input())

data = []
dp = []
for i in range(n):
    part = list(map(int,input().split()))
    m = len(part)
    data.append(part)
    dp.append([0 for _ in range(m)])

dp[0][0] = data[0][0]
for j in range(1, n):
    leng = len(data[j])
    for k in range(leng):
        if k == 0:
            dp[j][0] =  data[j][0] + dp[j-1][0]
        elif k == leng-1:
            dp[j][k] = data[j][k] + dp[j-1][k-1]
        else:
            dp[j][k] = max(dp[j-1][k-1], dp[j-1][k]) + data[j][k]

print(max(dp[-1]))
