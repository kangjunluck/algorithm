import sys
from collections import deque

n, m = map(int,input().split())

dc = [2, -2, -1, 1]
dr = [1, 1, 2, 2]

q = deque()
q.append((0, 0, 1))
max = 0
out = 0
while q:
    now = q.popleft()
    if now[2] > max:
        max = now[2]
    if now[2] < 5:
        for arr in range(4):
            nextC = now[0] + dc[arr]
            nextR = now[1] + dr[arr]
            if 0<=nextC<n and 0<=nextR<m:
                if now[2] == 4:
                    if nextC == 0 and nextR == 6:
                        q.append((nextC, nextR, now[2]+1))
                else:        
                    q.append((nextC, nextR, now[2]+1))
    else:
        out = 1
        break
if out == 1:
    max = m-2

print(max)