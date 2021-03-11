import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

board = [list(map(str,input().strip())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(a, b, cnt = 1):
    global ans
    if a == 0 and b == m-1:
        if cnt == k:
            ans += 1
    for i in range(4):
        nextR = a + dr[i]
        nextC = b + dc[i]
        if 0<=nextR<n and 0<=nextC<m and board[nextR][nextC] == '.' and visited[nextR][nextC] == 0:
            visited[nextR][nextC] = 1
            dfs(nextR, nextC, cnt + 1)
            visited[nextR][nextC] = 0
            
ans = 0
visited[n-1][0] = 1
dfs(n-1, 0)
print(ans)
