import sys

input = sys.stdin.readline

n, m = map(int,input().split())

dp = [0] * 15
dp[0] = ['1']
dp[1] = ['1+1', '2']
dp[2] = ['1+1+1', '1+2', '2+1', '3']
k = 2
while k < n-1:
    dp[k+1] =[]
    for part1 in dp[k-2]:
        dp[k+1].append(part1 + '+3')
    for part2 in dp[k-1]:
        dp[k+1].append(part2 + '+2')
    for part3 in dp[k]:
        dp[k+1].append(part3 + '+1')
    k += 1
ans = sorted(dp[n-1])
result = 0
if m  > len(ans):
    result = -1
else:
    result = ans[m-1]
print(result)
