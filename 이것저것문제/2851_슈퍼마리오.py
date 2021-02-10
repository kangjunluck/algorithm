import sys

input = sys.stdin.readline

T = 10
sum = 0
ans = 0
for step in range(1, T+1):
    now = int(input())
    sum += now
    ans = sum
    if sum >= 100:
        before = 100 - (sum-now)
        after = sum - 100
        if before >= after:
            ans = sum
        else:
            ans = sum - now
        break
print(ans)   