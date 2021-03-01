import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline
board = [list(map(str, input().split())) for _ in range(5)]

ans = []

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(a, b, word=''):
    word += board[a][b]
    if len(word) == 6:
        ans.append(word)
        return
    for i in range(4):
        nextR = a + dr[i]
        nextC = b + dc[i]
        if 0<= nextR< 5 and 0<= nextC < 5:
            dfs(nextR, nextC, word)
        
for i in range(5):
    for j in range(5):
        dfs(i, j)
print(len(set(ans)))