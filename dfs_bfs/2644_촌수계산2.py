import sys
from collections import deque

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

def bfs(i):
    q = deque()
    q.append((i, 0))
    visited[i] = 1
    ans = -1
    while q:
        now = q.popleft()
        cnt = now[1]
        if now[0] == end:
            ans = cnt
            break
        for rel in relation[now[0]]:
            if visited[rel]: continue
            visited[rel] = 1
            q.append((rel, cnt+1))
    return ans

print(bfs(start))