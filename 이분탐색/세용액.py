#nlogn이 될 거 같은데
# 기존대로 한바퀴만 돌리고 가운데 값은 이분탐색으로?
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 3000000000
for i in range(n):
    one = data[i]
    l = 0
    r = n-1 
    while l < r:
        if l == i:
            l += 1
            continue
        if r == i:
            r -= 1
            continue
        total = data[l] + data[r]
        if abs(total + one) < result:
            answer = [data[l], data[r], one]
            answer.sort()
            result = abs(total + one)
        if total + one < 0: l += 1
        else: r -= 1
for i in range(3):
    if i == 2:
        print(answer[i])
    else:
        print(answer[i], end=" ")