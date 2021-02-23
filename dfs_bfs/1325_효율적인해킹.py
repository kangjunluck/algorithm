import sys

input = sys.stdin.readline

def dfs(i):
    sum = 1
    for w in board[i]:
        if visited[w] == 0:
            visited[w] = 1
            sum += dfs(w)
    return sum

n, m = map(int,input().split())
board = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    board[b].append(a)

result = []
maxi = 0
isstart = [0 for _ in range(n+1)]
for start in range(1,n+1):
    if isstart[start]: continue
    isstart[start] = 1
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    part = dfs(start)
    if part > maxi:
        maxi = part
        result = [start]
    elif part == maxi:
        result.append(start)

print(*result)