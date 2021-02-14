import sys

input = sys.stdin.readline

n, m = map(int,input().split())
box = list(map(int,input().split()))
dp = [0]*n
for i in range(n):
    if i == 0:
        dp[i] = box[i]
    else:
        dp[i] = dp[i-1] + box[i]

for case in range(m):
    ans = 0
    start, end = map(int, input().split())
    if start-2 < 0:
        ans = dp[end-1]
    else:
        ans = dp[end-1] - dp[start-2]
    print(ans)