##재귀함수인거같은데 dfs
import sys

sys.stdin=open("organic.txt","r")

case = int(sys.stdin.readline())

for k in range(case):

    n,m,v=map(int, sys.stdin.readline().split())

    board=[[0 for _ in range(n)] for _ in range(m)]

    a=[]
    for _ in range(v):
        a.append(list(map(int, sys.stdin.readline().split())))

    for i,j in a:
        board[j][i]=1

    visited=[[0 for _ in range(n)] for _ in range(m)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    def dfs(r, c) :        #재귀 함수 정의
        
        visited[r][c] = 1
                
        for i in range(4) :
            nextR = r+dr[i]
            nextC = c+dc[i]
            
            if 0<=nextR<m and 0<=nextC<n :
                if visited[nextR][nextC]==0 and board[nextR][nextC]==1 :
                    dfs(nextR, nextC)

        return

    ans = 0

    for i in range(m) :
        for j in range(n) :
            if board[i][j]==1 and visited[i][j]==0 :
                dfs(i, j)
                ans+=1

    print(ans)