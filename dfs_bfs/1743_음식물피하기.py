import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

n, m, v = map(int,input().split())
board = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dc = [1, -1, 0, 0]
dr = [0, 0, 1, -1]

def dfs(a, b):
    ans = 1
    for k in range(4):
        nextR = a + dr[k]
        nextC = b + dc[k]
        if 0 <= nextR < n and 0<= nextC < m and visited[nextR][nextC] == 0 and board[nextR][nextC] == 1:
            visited[nextR][nextC] = 1
            ans += dfs(nextR, nextC)
    return ans

for __ in range(v):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1
maxi = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            visited[i][j] = 1
            answer = dfs(i, j)
            if answer > maxi:
                maxi = answer
print(maxi)