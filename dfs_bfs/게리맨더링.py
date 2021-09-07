import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
numbers = [0] + numbers
data = [[] for _ in range(n+1)]
for i in range(1, n+1):
    next = list(map(int,input().split()))
    for j in range(1, next[0]+1):
        data[i].append(next[j])
def bfs(sel):
    start = sel[0]
    q = deque()
    visited = [0] * (n+1)
    visited[start] = 1
    q.append(start)
    cnt = 1
    while q:
        now = q.popleft()
        for nx in data[now]:
            if nx in sel and visited[nx] != 1:
                visited[nx] = 1
                q.append(nx)
                cnt += 1
    if cnt == len(sel):
        return True
    else:
        return False

def perm(idx, start, size):
    global result
    if idx == size:
        sel2 = []
        for j in range(1,n+1):
            if j not in sel:
                sel2.append(j)
        # sel, sel2 가 bfs로 연결되어 있는가?
        if bfs(sel) and bfs(sel2):
            sum1 = 0
            for aa in sel:
                sum1 += numbers[aa]
            sum2 = 0
            for bb in sel2:
                sum2 += numbers[bb]
            answer = abs(sum1 - sum2)
            result = min(result, answer)
        return
    for i in range(start, n+1):
        sel.append(i)
        perm(idx+1, i+1, size)
        sel.pop()

# 두개로 나눈다음에, 
result = 100000000
for size in range(1, n//2 + 1):
    sel = []
    perm(0, 1, size)

if result == 100000000:
    print(-1)
else:
    print(result)
