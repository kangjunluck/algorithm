import sys

input = sys.stdin.readline

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    data = [list(map(int,input().split())) for _ in range(2)]
    
    dp0 = [0 for _ in range(n)]
    dp1 = [0 for _ in range(n)]
    dp0[0] = data[0][0]
    dp1[0] = data[1][0]
    dp0[1] = dp1[0] + data[0][1]
    dp1[1] = dp0[0] + data[1][1]
    for i in range(2, n):
        dp0[i] = max(dp1[i-1], dp1[i-2], dp0[i-2]) + data[0][i]
        dp1[i] = max(dp0[i-1], dp0[i-2], dp1[i-2]) + data[1][i]
    print(max(dp0[n-1], dp1[n-1]))


