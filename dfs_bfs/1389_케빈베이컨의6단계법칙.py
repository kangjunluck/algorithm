import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

visited = [0 for _ in range(n+1)]

cabin = [0 for _ in range(n+1)]
cabin[0] = 1000
min = 10000
ans = 0
for j in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    visited[j] = 1
    q = [(j, 0)]
    while q:
        now = q.pop(0)
        cabin[j] += now[1]
        for k in board[now[0]]:
            if visited[k]: continue
            visited[k] = 1
            q.append((k, now[1]+1))
    if cabin[j] < min:
        min = cabin[j]
        ans = j
print(ans)



