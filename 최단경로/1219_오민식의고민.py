import sys

input = sys.stdin.readline

n, start, end, m = map(int,input().split())
data = []

for _ in range(m):
    a, b, t = map(int, input().split())
    data.append((a, b, -t))

income = list(map(int, input().split()))

INF = sys.maxsize
ans = [-INF for _ in range(n)]
ans[start] = income[start]
def bellman(start, end):
    for o in range(n-1):
        for i in range(m):
            s, e, w = data[i]
            iincome = income[e]
            sumw = w + iincome + ans[s]
            if sumw > ans[e]:
                ans[e] = sumw
    for i in range(m):
        s, e, w = data[i]
        iincome = income[e]
        sumw = w + iincome + ans[s]
        if sumw > ans[e]:
            return True
    return False
result = bellman(start, end)
if ans[end] == -INF:
    print('gg')
else:
    if result:
        print('Gee')
    else:
        print(ans[end])