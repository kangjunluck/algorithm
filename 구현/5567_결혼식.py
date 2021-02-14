import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
rel = int(input())
board = [[] for _ in range(n+1)]
for i in range(rel):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

visited = [0]*(n+1)
q = deque()
q.append((1, 2))
visited[1] = 1
result = 0
while q:
    now = q.popleft()
    point, cnt = now[0], now[1]
    for i in board[point]:
        if visited[i] == 1:
            continue
        else:
            if cnt-1 >= 0:
                q.append((i, cnt-1))
                visited[i] = 1
                result += 1
print(result)