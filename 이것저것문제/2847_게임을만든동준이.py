import sys

input = sys.stdin.readline

n = int(input())

result = []
ans = 0

for i in range(n):
    result.append(int(input()))

start = 20000
for j in range(n):
    now = result.pop()
    if now >= start:
        ans += now - start + 1
        start = start - 1
    else:
        start = now
print(ans)

    