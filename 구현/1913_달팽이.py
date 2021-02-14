import sys

input = sys.stdin.readline

n = int(input())
check = int(input())

ind = (n-1)//2
# dp 인가
# 2n + 1
dp = []
dp.append([[1]])
dp.append([[9, 2, 3], [8, 1, 4], [7, 6, 5]])

if ind <= 1:
    pass
else:
    for k in range(2, ind+1):
        before = dp[k-1]
        result = [[]] + before +[[]]
        for i in range(2*k+1):
            result[i] = [(2*k+1)**2 - i] + result[i]
        for j in range(2*k+1-1):
            result[0].append((2*k-1)**2 + (j+1))
        for m in range(1, 2*k +1):
            result[-1].append(result[-1][0]-m)
        for o in range(1, 2*k):
            result[o].append(result[0][-1]+ o)
        dp.append(result)
ans = dp[ind]
result = []
for a in range(n):
    for b in range(n):
        if ans[a][b] == check:
            result.append((a+1, b+1))

for step in ans:
    print(' '.join((str(step)[1:-1].split(', '))))
print(result[0][0], result[0][1])