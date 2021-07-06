n, m = map(int, input().split())

board = [list(map(str, input().strip())) for _ in range(n)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
answer = 0
alphas = [0] * 26
def dfs(i, j, cnt):
    global answer
    answer = max(answer, cnt)
    for ar in range(4):
        nextR = i + dr[ar]
        nextC = j + dc[ar]
        if 0 <= nextR < n and 0<= nextC < m and alphas[ord(board[nextR][nextC])-65] == 0:
            alphas[ord(board[nextR][nextC])-65] = 1
            dfs(nextR, nextC, cnt + 1)
            alphas[ord(board[nextR][nextC])-65] = 0
alphas[ord(board[0][0])-65] = 1
dfs(0, 0, 1)
print(answer)

##################################################################
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(str, input().strip())) for _ in range(n)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
answer = 0
visited = [[0]*m for _ in range(n)]
def dfs(i, j, alphas, cnt):
    global answer
    answer = max(answer, cnt)
    for ar in range(4):
        nextR = i + dr[ar]
        nextC = j + dc[ar]
        if 0 <= nextR < n and 0<= nextC < m and board[nextR][nextC] not in alphas:
            alphas.append(board[nextR][nextC])
            dfs(nextR, nextC, alphas, cnt + 1)
            alphas.pop()
dfs(0, 0, [board[0][0]], 1)
print(answer)
