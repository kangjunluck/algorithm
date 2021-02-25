import sys

input = sys.stdin.readline

n = int(input())

numbers = list(map(int,input().split()))
a, b = map(int,input().split())

ans = n
for i in range(n):
    if numbers[i]-a > 0:
        ans += (numbers[i]-a) // b
        if (numbers[i]-a) % b:
            ans += 1

print(ans)