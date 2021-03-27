import sys

input = sys.stdin.readline

n, m = map(int, input().split())

data = []
for _ in range(m):
    a, b, c = map(int,input().split())
    data.append((a, b, c))
INF = sys.maxsize
ans = [INF for _ in range(n+1)]
ans[1] = 0

def bellman(start):
    # 최대 n-1번 돌려야 경로가 지정될 수 있다. 그 이상으로 변하면, cycle이 된다. - 무한으로
    for no in range(n-1):
        for i in range(m):
            s, e, t = data[i]
            sumt = ans[s] + t
            if sumt < ans[e] and ans[s] != INF:
                ans[e] = sumt
    for i in range(m):
        s, e, t = data[i]
        sumt = ans[s] + t
        if sumt < ans[e] and ans[s] != INF:
            ans[e] = sumt
            return True   # -로 계속 커진다. cycle이다
    return False # 값이 일정한 최소 경로가 나온다.

if bellman(1):
    print(-1)
else:
    for j in range(2, n+1):
        if ans[j] == INF:
            print(-1)
        else:
            print(ans[j])

