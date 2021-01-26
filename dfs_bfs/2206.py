import sys
from collections import deque
import copy

sys.stdin = open('2206.txt','r')
input = sys.stdin.readline
n, m =map(int, input().split())

board_start = []
for _ in range(n):
    board_start.append(list(map(int,input().strip())))
# 시작점은 board(0)(0)
# 도착점은 board(n)(m)

dc = [1, -1, 0, 0]
dr = [0, 0, 1, -1]

result = []
for i in range(n):
    for j in range(m):
        board = copy.deepcopy(board_start)
        board[i][j]=0
        q = deque()
        q.append((0, 0, 0))
        board[0][0]=1
        ans = 0
        while q:
            now = q.popleft()
            
            for arrow in range(4):
                nextC = now[0] + dc[arrow]
                nextR = now[1] + dr[arrow]
                if nextC == n-1 and nextR == m-1:
                    ans = now[2] + 2
                    break

                if 0<=nextC<n and 0<=nextR<m and board[nextC][nextR] == 0:
                    board[nextC][nextR] = 1
                    q.append((nextC, nextR, now[2]+1))
        
        result.append(ans)
if len(result) == result.count(0):
    print(-1)
else:
    change_list = [re for re in result if re > 0]
    print(min(change_list))