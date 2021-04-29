import sys

input = sys.stdin.readline

n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]

dp1 = [0 for _ in range(n)]
dp2 = [0 for _ in range(n)]
dp3 = [0 for _ in range(n)]

dp1[0] = data[0][0]
dp2[0] = data[0][1]
dp3[0] = data[0][2]

i = 1
while i < n:
    dp1[i] = data[i][0] + min(dp2[i-1], dp3[i-1])
    dp2[i] = data[i][1] + min(dp1[i-1], dp3[i-1])
    dp3[i] = data[i][2] + min(dp1[i-1], dp2[i-1])
    i += 1

print(min(dp1[-1], dp2[-1], dp3[-1]))
