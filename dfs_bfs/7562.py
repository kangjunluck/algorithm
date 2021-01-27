# 최소 거리 계산이기 때문에 bfs를 쓸 것 같다. 100 * 100 이라 dfs로 해야할 것 같다. 시간 초과가 난다

 ################################################
import sys
from collections import deque

sys.stdin = open('7562.txt', 'r')
input = sys.stdin.readline

case = int(input())

dr = [1, 1, 2, 2, -1, -1, -2, -2]
dc = [2, -2, 1, -1, 2, -2, 1, -1]

for i in range(case):
    n = int(input())
    a, b = list(map(int, input().split())) # 시작지점
    x, y = list(map(int, input().split())) # 도착지점
    
    if (a,b)==(x,y):
        print(0)
    else:
        visited = [[0 for _ in range(n)] for __ in range(n)]
        visited[a][b] = 1
        q = deque()
        q.append((a,b,0))
        while q:
            c, r, cnt = q.popleft()
            if (c, r) == (x, y):             
                break
            for j in range(8):
                nextC = c + dc[j]
                nextR = r + dr[j]
                if 0<=nextC<n and 0<=nextR<n and visited[nextC][nextR] == 0:
                    visited[nextC][nextR] = 1
                    q.append((nextC, nextR, cnt+1))
                                   
        print(cnt)


# import sys
# from collections import deque

# input = sys.stdin.readline

# c = int(input())
# ans = []

# dR = 1, 2, 2, 1, -1, -2, -2, -1
# dC = 2, 1, -1, -2, -2, -1, 1, 2

# for _ in range(c) :
#     n = int(input())
#     sR, sC = map(int, input().split())
#     eR, eC = map(int, input().split())

#     visited = [[ 0 for _ in range(n)] for _ in range(n)]
#     que = deque()
#     que.append((sR, sC, 0))
#     visited[sR][sC]=1
#     while que :
#         r, c, count = que.popleft()
#         if r==eR and c==eC : break
#         for i in range(8) :
#             nR, nC = r+dR[i], c+dC[i]
#             if 0<=nR<n and 0<=nC<n and not visited[nR][nC] :
#                 visited[nR][nC] = 1
#                 que.append((nR,nC,count+1))
#     ans.append(count)

# print('\n'.join(map(str, ans)))        