# 최소거리 계산, bfs로 풀어야할 것 같다. que 이용해서, 다익스트라?
# 6 4
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1
import sys

sys.stdin=open("tomato.txt","r")

m, n = map(int, sys.stdin.readline().split())

board=[]
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

# 시작 위치를 알아야할 것 같다.
for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            si,sj=i,j  # 3,5이겟지
q=[(si,sj,0)]
visited = [[0 for _ in range(m)] for _ in range(n)]


di = [0, 1, 0, -1] #아래 위
dj = [1, 0, -1, 0] #오른쪽 왼쪽

while q :
    now = q.pop()
    for i in range(4):
        nexti, nextj = now[0]+di[i],now[1]+dj[i]
        
        if 0<=nexti<n and 0<=nextj<m and visited[nexti][nextj]==0 and board[nexti][nextj]==0:
            q = [(nexti,nextj,now[2]+1)]+q
            visited[nexti][nextj]=now[2]+1
# 이러면 한붓그리기 같이 되어 버린다.... ?

print(visited)



# from collections import deque

# import sys
# from collections import deque

# input = sys.stdin.readline

# m, n = map(int, input().split())
# board = []
# que = deque()

# for i in range(n) :
#     board.append(list(map(int, input().split())))
#     for j in range(m) :
#         if board[i][j]==1 :
#             que.append((i, j, 0))

# def isFinished() :
#     for i in range(n) :
#         for j in range(m) :
#             if board[i][j]==0 :
#                 return False
#     return True

# ans = 0
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]

# while que :
#     r,c,count = que.popleft()

#     for i in range(n) :
#         print(board[i])

#     print("-------------------------------")
    
#     for i in range(4) :
#         nextR, nextC = r+dr[i], c+dc[i]
#         if 0<=nextR<n and 0<=nextC<m and board[nextR][nextC]==0 :
#             board[nextR][nextC]=1
#             ans = count+1
#             que.append((nextR, nextC, ans))


# if isFinished() : print(ans)
# else : print(-1)
    