T = int(input())

for tc in range(1,T+1):
    n, a, b = map(int, input().split())
    maxi = min(a, b)
    mini = a+b
    if a+b >= n:
        mini = a + b - n
    else:
        mini = 0
    print('#{} {} {}'.format(tc, maxi, mini))