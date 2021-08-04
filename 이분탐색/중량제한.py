from collections import deque

n, m = map(int, input().split())
data = [[] for _ in range(n+1)]
mini = 1000000000
maxi = 0
for _ in range(n):
    a, b, c = map(int,input().split())
    data[a].append((b, c))
    data[b].append((a, c))
    mini = min(mini, c)
    maxi = max(maxi, c)
s, e = map(int,input().split())

def check(mid):
    visited = [0] * (n+1)
    visited[s] = 1
    q = deque()
    q.append(s)
    result = False
    while q:
        now = q.popleft()
        if now == e:
            result = True
            break
        for next, w in data[s]:
            if visited[next]: continue
            if w <=mid:
                visited[next] = 1
                q.append(next)
    return result

while mini < maxi:
    mid = (mini+maxi)//2
    if check(mid): mini = mid+1
    else: maxi = mid

print(mid+1)