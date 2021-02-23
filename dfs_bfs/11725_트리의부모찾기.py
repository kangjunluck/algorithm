import sys

input = sys.stdin.readline

n = int(input())

board = [[] for _ in range(n+1)]

for make in range(n-1):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)
visited = [0 for _ in range(n+1)]

ans = [0 for _ in range(n-1)]
v = 1
s = []
s.append(v)
visited[v] = 1
while s:
    for w in board[v]:
        if visited[w] == 0:
            ans[w-2] = v
            s.append(v)
            visited[w] = 1
            v = w
            break
    else:
        v = s.pop()
for i in ans:
    print(i)