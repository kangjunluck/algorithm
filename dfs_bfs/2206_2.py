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
q.append((0, 0, 0, 0))
board[0][0]=2
ans = 0
while q:
    now = q.popleft()
    
    for arrow in range(4):
        nextC = now[0] + dc[arrow]
        nextR = now[1] + dr[arrow]
        if nextC == n-1 and nextR == m-1:
            ans = now[2] + 2
            break
        elif 0<=nextC<n and 0<=nextR<m:
            if now[3]==0 and board[nextC][nextR] == 1:
                board[nextC][nextR] = 2
                q.append((nextC, nextR, now[2]+1, 1))
            elif board[nextC][nextR] == 0:
                board[nextC][nextR] = 2
                q.append((nextC, nextR, now[2]+1, now[3]))
            else:
                pass
        else:
            pass
        
if ans ==0:
    print(-1)
else:
    print(ans)
# if len(result) == result.count(0):
#     print(-1)
# else:
#     change_list = [re for re in result if re > 0]
#     print(min(change_list))