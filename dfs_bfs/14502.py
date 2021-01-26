#bfs로 풀어야할 것 같다. que 이용하자.
import sys
import copy

from itertools import combinations
from collections import deque


sys.stdin=open('14502.txt',"r")
input = sys.stdin.readline

n, m = map(int, input().split())

#모든 경우의 수를 하여 0의 갯수를 샌 다음 최댓값 찾기? 조합 필요?
#board 만들기
board_start = []
for i in range(n):
    board_start.append(list(map(int, input().split())))

#시작점 찾기 및 0인 점 찾기 
que_start = deque()
zero_list = []
for i in range(n):
    for j in range(m):
        if board_start[i][j]==2:
            que_start.append((i,j))
        elif board_start[i][j]==0:
            zero_list.append((i,j))

# 0의 갯수 세기 함수
def isFinished() :
    cnt=0
    for i in range(n) :
        for j in range(m) :
            if board[i][j]==0 :
                cnt+=1
    return cnt

# 조합의 경우의 수  안전한 영역 수를 담는 그릇
compare_list=[]

# 조합, 0의 자리들 중 1로 바꿀 위치 고르기.
for combination in combinations(zero_list, 3):
    board = copy.deepcopy(board_start)
    que= deque(que_start)
    for a,b in combination:
        board[a][b]=1
 
# bfs 루트 시작

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    while que :
        c,r = que.popleft()
        
        for i in range(4) :
            nextC, nextR = c+dc[i], r+dr[i]
            if 0<=nextC<n and 0<=nextR<m and board[nextC][nextR]==0 :
                board[nextC][nextR]=2
                que.append((nextC, nextR))
    
    k=isFinished()
    compare_list.append(k)
  

print(max(compare_list))



# import sys
# from collections import deque

# input = sys.stdin.readline

# n, m = map(int, input().split())

# board = []
# virus = []
# empty = []

# for i in range(n) :
#     board.append(list(map(int, input().split())))
#     for j,a in enumerate(board[i]) :
#         if a==2 : virus.append((i,j))
#         elif a==0 : empty.append((i,j))

# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
# ans = 0

# for i in range(len(empty)) :
#     board[empty[i][0]][empty[i][1]]=1
#     for j in range(i+1,len(empty)) :
#         board[empty[j][0]][empty[j][1]]=1
#         for k in range(j+1,len(empty)) :
#             board[empty[k][0]][empty[k][1]]=1

#             visited = [ [ 0 for _ in range(m)] for _ in range(n) ]
#             que = deque(virus)

#             count=len(empty)-3
            
#             while que :
#                 r, c = que.popleft()
#                 for p in range(4) :
#                     nextR, nextC = r+dr[p], c+dc[p]
#                     if 0<=nextR<n and 0<=nextC<m and not visited[nextR][nextC] and not board[nextR][nextC] :
#                         count-=1
#                         visited[nextR][nextC]=1
#                         que.append((nextR,nextC))
                        
#             ans = max(ans, count)

#             board[empty[k][0]][empty[k][1]]=0
#         board[empty[j][0]][empty[j][1]]=0
#     board[empty[i][0]][empty[i][1]]=0

# print(ans)