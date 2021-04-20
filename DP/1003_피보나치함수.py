import sys

input = sys.stdin.readline

T = int(input())

dp = []
dp0 = [-1 for _ in range(41)]
dp1 = [-1 for _ in range(41)]
dp0[0] = dp1[1] = 1
dp0[1] = dp1[0] = 0
for tc in range(1,T+1):
    n = int(input())
    if n <= 1:
        pass
    else:
        i = 2
        while i<=n:
            dp0[i] = dp0[i-1] + dp0[i-2]
            dp1[i] = dp1[i-1] + dp1[i-2]
            i+=1
    print(dp0[n], dp1[n])