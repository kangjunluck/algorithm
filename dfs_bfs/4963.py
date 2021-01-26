import sys

sys.stdin=open('4963.txt',"r")
input = sys.stdin.readline


def dfs(j, i):
    visited[j][i]=1
    dr = [0, 1, 0, -1, -1, 1, -1, 1]
    dc = [1, 0, -1, 0, 1, 1, -1, -1]
    for array in range(8):
        nextC = j + dc[array]
        nextR = i + dr[array]

        if 0<=nextC<m and 0<=nextR<n and visited[nextC][nextR]==0 and board[nextC][nextR]==1:
            dfs(nextC, nextR)
    return    


while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break

    else:
        board = []
        
        visited=[[0 for _ in range(n)] for _ in range(m)]

        for i in range(m) :
            board.append(list(map(int, sys.stdin.readline().split())))
        ans=0
        for a in range(m):
            for b in range(n):
                if visited[a][b]==0 and board[a][b]==1:
                    ans+=1
                    dfs(a, b)
        print(ans)