import sys

input = sys.stdin.readline

n = int(input())
parentdata = list(map(int,input().split()))
delete = int(input())

board = [[] for _ in range(n)]
visited = [ 0 for _ in range(n)]

start = -1
for i in range(n):
    if parentdata[i] == -1:
        start = i
        continue
    board[parentdata[i]].append(i)
s = []
v = start
s.append(v)
visited[v] = 1
ans = 0
if v == delete:
    pass
else: 
    while s:
        now = s.pop()
        cnt = 0
        for w in board[now]:
            if w == delete:
                continue
            if visited[w] == 0:
                cnt += 1
                s.append(w)
                visited[w] = 1                
        if cnt == 0:
            ans += 1
        else:
            pass
            

print(ans)