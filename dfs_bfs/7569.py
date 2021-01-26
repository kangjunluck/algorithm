import sys
from collections import deque

sys.stdin=open('7569.txt', 'r')
input=sys.stdin.readline
n, m, h = map(int, input().split())

que = deque()
board=[[] for _ in range(h)]
for i in range(h):
    for j in range(m):
        board[i].append(list(map(int, input().split())))
        for k in range(n):
            if board[i][j][k] == 1:
                que.append((i, j, k, 0))

dh = [1, -1, 0, 0, 0, 0]
dc = [0, 0, 1, -1, 0, 0]
dr = [0, 0, 0, 0, 1, -1]

ans=0
while que:
    now=que.popleft()  
    for arrow in range(6):
        nextH = now[0] + dh[arrow]
        nextC = now[1] + dc[arrow]
        nextR = now[2] + dr[arrow]

        if 0<=nextH<h and 0<=nextC<m and 0<=nextR<n and board[nextH][nextC][nextR]==0:
            board[nextH][nextC][nextR]=1
            ans = now[3] + 1
            que.append((nextH, nextC, nextR, ans))
           
def finish():
    for aa in range(n):
        for bb in range(m):
            for cc in range(h):
                if board[cc][bb][aa]==0:
                    return False
    return True

if finish():
    print(ans)
else: print(-1)