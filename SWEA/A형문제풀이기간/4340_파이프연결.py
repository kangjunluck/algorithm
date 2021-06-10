T = int(input())

dr = [1, -1]

for tc in range(1,T+1):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[0][0] = 1

    mini = 1000000
    # ->11  12<- 내려오는거 13 올라온거 14

    def dfs(a, b, before = 11, cnt = 1):
        global mini
        if cnt > mini:
            return
        if a == n-1 and b == n-1:
            if before == 13 and ( board[a][b] == 3 or board[a][b] == 4 or board[a][b] == 5 or board[a][b] == 6 ):
                mini = min(mini, cnt)
            elif before == 11 and ( board[a][b] == 1 or board[a][b] == 2 ):
                mini = min(mini, cnt)
            return
        
        if before == 11:
            if board[a][b] == 1 or board[a][b] == 2:
                if b+1 <= n-1 and visited[a][b+1] == 0:
                    if board[a][b+1] != 0:
                        visited[a][b+1] = 1
                        dfs(a, b+1, 11, cnt+1)
                        visited[a][b+1] = 0
            else:
                for ar in range(2):
                    nextA = a + dr[ar]
                    if 0 <= nextA <= n-1 and visited[nextA][b] == 0:
                        if board[nextA][b] != 0:
                            visited[nextA][b] = 1
                            if ar == 0:
                                dfs(nextA, b, 13, cnt+1)
                            else:
                                dfs(nextA, b, 14, cnt+1)
                            visited[nextA][b] = 0       
        elif before == 12:
            if board[a][b] == 1 or board[a][b] == 2:
                if 0<=b-1 and visited[a][b-1] == 0:
                    if board[a][b-1] != 0:
                        visited[a][b-1] = 1
                        dfs(a, b-1, 12, cnt+1)
                        visited[a][b-1] = 0
            else:
                for ar in range(2):
                    nextA = a + dr[ar]
                    if 0 <= nextA <= n-1 and visited[nextA][b] == 0:
                        if board[nextA][b] != 0:
                            visited[nextA][b] = 1
                            if ar == 0:
                                dfs(nextA, b, 13, cnt+1)
                            else:
                                dfs(nextA, b, 14, cnt+1)
                            visited[nextA][b] = 0
        elif before == 13:
            if board[a][b] == 1 or board[a][b] == 2:
                if a+1 <= n-1 and visited[a+1][b] == 0:
                    if board[a+1][b] != 0:
                        visited[a+1][b] = 1
                        dfs(a+1, b, 13, cnt+1)
                        visited[a+1][b] = 0
            else:
                for ar in range(2):
                    nextB = b + dr[ar]
                    if 0 <= nextB <= n-1 and visited[a][nextB] == 0:
                        if board[a][nextB] != 0:
                            visited[a][nextB] = 1
                            if ar == 0:
                                dfs(a, nextB, 11, cnt+1)
                            else:
                                dfs(a, nextB, 12, cnt+1)
                            visited[a][nextB] = 0
        else:
            if board[a][b] == 1 or board[a][b] == 2:
                if 0<=a-1 and visited[a-1][b] == 0:
                    if board[a-1][b] != 0:
                        visited[a-1][b] = 1
                        dfs(a-1, b, 14, cnt+1)
                        visited[a-1][b] = 0
            else:
                for ar in range(2):
                    nextB = b + dr[ar]
                    if 0 <= nextB <= n-1 and visited[a][nextB] == 0:
                        if board[a][nextB] != 0:
                            visited[a][nextB] = 1
                            if ar == 0:
                                dfs(a, nextB, 11, cnt+1)
                            else:
                                dfs(a, nextB, 12, cnt+1)
                            visited[a][nextB] = 0
        return

    dfs(0, 0)

    print('#%d %d' %(tc, mini))