import sys

sys.stdin=open('2583.txt',"r")
input = sys.stdin.readline
n, m, k =map(int, input().split())

board = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            board[j][i]=1


visited=[[0 for _ in range(m)] for _ in range(n)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def dfs(j, i):
    visited[j][i]=1
    area = 1

    for array in range(4):
        nextC = j + dc[array]
        nextR = i + dr[array]

        if 0<=nextC<n and 0<=nextR<m and visited[nextC][nextR]==0 and board[nextC][nextR]==0:
            area+=dfs(nextC, nextR)
    return area

ans=0
area_list=[]
for x in range(m):
    for y in range(n):
        if visited[y][x]==0 and board[y][x]==0:
            ans+=1
            area_list.append(dfs(y, x))
area_list.sort()

print(ans)
for a in area_list:
    print(a, end=' ')