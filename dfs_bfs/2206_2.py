import sys
from collections import deque

sys.stdin = open('2206.txt','r')
input = sys.stdin.readline
n, m =map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int,input().strip())))
# 시작점은 board(0)(0)
# 도착점은 board(n)(m)

dc = [1, -1, 0, 0]
dr = [0, 0, 1, -1]

result = []

q = deque()
q.append((0, 0, 0, 1))
board[0][0]=2
ans = 0
visited = [[0 for _ in range(m)] for __ in range(n)]
while q:
    x, y, cnt, boom = q.popleft()
    if x == n-1 and y == m-1:
        ans = cnt + 1
        break
    for arrow in range(4):
        nextC = x + dc[arrow]
        nextR = y + dr[arrow]
        
        if 0<=nextC<n and 0<=nextR<m:
            if board[nextC][nextR] == 0:
                if not visited[nextC][nextR] or visited[nextC][nextR] > boom:
                    visited[nextC][nextR] = boom
                    q.append((nextC, nextR, cnt+1, boom))
            elif boom == 1:
                visited[nextC][nextR] = boom + 1
                q. append((nextC, nextR, cnt+1, boom + 1))
            else:
                pass
        else:
            pass
        
if ans ==0:
    print(-1)
else:
    print(ans)





#########################################
# import sys
# from collections import deque

# input = sys.stdin.readline

# n, m = map(int, input().split())
# board = []

# for i in range(n) :
#     board.append(list(map(int, input().strip())))
    
# visited = [[0 for _ in range(m)] for _ in range(n)]

# dr = 0, 1, 0, -1
# dc = 1, 0, -1, 0

# que = deque()
# que.append((0,0,1,1))
# visited[0][0]=1
# finish = False

# while que :
#     r, c, boom, count = que.popleft()
#     if r==n-1 and c==m-1 : 
#         finish=True
#         break
#     for i in range(4) :
#         nr, nc = r+dr[i], c+dc[i]
#         if 0<=nr<n and 0<=nc<m :
#             if board[nr][nc]==0 :
#                 if not visited[nr][nc] or visited[nr][nc]>boom :
#                     visited[nr][nc]=boom
#                     que.append((nr, nc, boom, count+1))
#             elif boom==1 :
#                 visited[nr][nc]=boom+1
#                 que.append((nr, nc, boom+1, count+1))

# if finish : print(count)
# else : print(-1)