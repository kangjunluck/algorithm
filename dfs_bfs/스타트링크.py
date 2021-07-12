import sys
from collections import deque

f, s, g, u, d = map(int,input().split())
cnts = [-1 for _ in range(f+1)]
q = deque()
q.append((s,0))
while q:
    i, cnt = q.popleft()
    if i == g:
        continue
    up = i + u
    down = i - d
    if up <= f:
        if cnts[up] == -1:
            cnts[up] = cnt + 1
            q.append((up, cnt+1))
        else:
            if cnts[up] > cnt + 1:
                cnts[up] = cnt + 1
                q.append((up, cnt+1))
    if 0 < down:
        if cnts[down] == -1:
            cnts[down] = cnt + 1
            q.append((down, cnt+1))
        else:
            if cnts[down] > cnt+1:
                cnts[down] = cnt+1
                q.append((down, cnt+1))
cnts[s] = 0
if cnts[g] == -1:
    print('use the stairs')
else:
    print(cnts[g])