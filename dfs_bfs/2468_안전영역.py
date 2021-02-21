import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
def dfs(a, b, start):
    for m in range(4):
        nextR = a + dr[m]
        nextC = b + dc[m]
        if 0<= nextR <n and 0<= nextC <n and visited[nextR][nextC] == 0 and board[nextR][nextC] > start:
            visited[nextR][nextC] = 1
            dfs(nextR, nextC, start)
    return True

start = 0
max = 0
while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > start and visited[i][j] == 0:
                visited[i][j] = 1
                if dfs(i, j, start):
                    ans += 1
    if ans == 0:
        break
    if ans > max:
        max = ans
    start += 1
print(max)