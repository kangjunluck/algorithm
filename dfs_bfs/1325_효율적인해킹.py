import sys

input = sys.stdin.readline

def dfs(i, word):
    global maxi
    word.append(i)
    if board[i] == []:
        if len(word)-1 >= maxi:
            maxi = len(word)-1
            ans.append(word[0])
            return
    else:
        for w in board[i]:
            if visited[w] == 0:
                visited[w] = 1
                dfs(w, word)
                visited[w] = 0
                word.pop()


n, m = map(int,input().split())
board = [ [] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    board[b].append(a)

ans = []
maxi = 0
# isstart = [0 for _ in range(n+1)]
for start in range(1,n+1):
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    word = []
    dfs(start, word)
    
print(*set(ans))