import sys
from collections import deque

sys.setrecursionlimit(100000)

n = int(input())

data = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    data[a].append((b, c))
    data[b].append((a, c))

parent = [0]*(n+1)
depth = [0]*(n+1)
visited = [0]*(n+1)
length = [0]*(n+1)

def dfs(i, dep, total):
    if depth[i] == 0: depth[i] = dep
    for next in data[i]:
        if visited[next[0]]: continue
        visited[next[0]] = 1
        parent[next[0]] = i
        length[next[0]] = total + next[1]
        dfs(next[0], dep+1, total + next[1])

dfs(1, 0, 0)


m = int(input())
for _ in range(m):
    s, e = map(int,input().split())
    if depth[s] > depth[e]: s, e = e, s
    gap = depth[e] - depth[s]
    total = length[s] + length[e]
    while gap > 0:
        e = parent[e]
        gap -= 1
    while s!=e:
        s = parent[s]
        e = parent[e]
    answer = total - 2*length[s]

    print(answer)


