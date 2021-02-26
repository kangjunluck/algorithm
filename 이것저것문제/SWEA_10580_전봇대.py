import sys

input = sys.stdin.readline

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    lines = []
    for i in range(n):
        a, b = map(int,input().split())
        lines.append((a, b))
    ans = 0
    for j in range(n-1):
        for k in range(j+1, n):
            if lines[j][0] > lines[k][0]:
                if lines[j][1] < lines[k][1]:
                    ans += 1
            else:
                if lines[j][1] > lines[k][1]:
                    ans += 1
    print('#{} {}'.format(tc, ans))
        