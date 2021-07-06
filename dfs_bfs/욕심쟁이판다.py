n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
dp = [[-1]*n for _ in range(n)]
def dfs(i, j):
    if dp[i][j] != -1: return dp[i][j]
    dp[i][j] = 1
    for ar in range(4):
        nextR = i + dr[ar]
        nextC = j + dc[ar]
        if 0 <= nextR < n and 0 <= nextC < n and board[nextR][nextC] > board[i][j]:
            dp[i][j] = max(dp[i][j], dfs(nextR, nextC)+1)
    return dp[i][j]
answer = 1
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)        

################################################################
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(i, j, cnt):
    global answer
    answer = max(answer, cnt)
    for ar in range(4):
        nextR = i + dr[ar]
        nextC = j + dc[ar]
        if 0 <= nextR < n and 0 <= nextC < n and board[nextR][nextC] > board[i][j]:
            dfs(nextR, nextC, cnt+1)
answer = 0
for i in range(n):
    for j in range(n):
        dfs(i ,j, 1)
print(answer)        
