from collections import deque

n = int(input())
c = [[] for _ in range(n+1)]


for _ in range(n-1):
    pa, ch, w = map(int,input().split())
    c[pa].append((ch, w))
    c[ch].append((pa, w))

    
v = [0 for _ in range(n+1)]
q = deque()
q.append((1, 0))
v[1] = 1
maxi = 0
l_node = 0
while q:
    now, nowlong = q.popleft()
    if maxi < nowlong:
        maxi = nowlong
        l_node = now
    for next, long in c[now]:
        if v[next] == 0:
            v[next] = 1
            q.append((next, nowlong + long))

q.append((l_node, 0))
v = [0 for _ in range(n+1)]
v[l_node] = 1
maxi = 0
while q:
    now, nowlong = q.popleft()
    if maxi < nowlong:
        maxi = nowlong
    for next, long in c[now]:
        if v[next] == 0:
            v[next] = 1
            q.append((next, nowlong + long))
print(maxi)