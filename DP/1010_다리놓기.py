import sys

input = sys.stdin.readline

T = int(input())

for tc in range(1,T+1):
    n, m = map(int,input().split())
    # mCn 아닌감
    ans = 1
    a = n
    i = 1
    while i <= a:
        ans *= m + 1 - i
        i += 1
    i = 1
    while i <= a:
        ans //= n + 1 - i
        i += 1
    print(ans)