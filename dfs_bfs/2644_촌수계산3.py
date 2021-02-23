import sys

input = sys.stdin.readline
n = int(input())
start, end = map(int,input().split())
m = int(input())

relation = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    relation[a].append(b)
    relation[b].append(a)
v = start
q = []
q.append((v, 0))
visited[v] = 1
ans = 0
while q:
    now = q.pop()
    node = now[0]
    cnt = now[1]
    if node == end:
        ans = cnt
        break
    for w in relation[node]:
        if visited[w] == 0:
            visited[w] = 1
            q.append((w, cnt+1))
if ans > 0:
    print(ans)
else:
    print(-1)