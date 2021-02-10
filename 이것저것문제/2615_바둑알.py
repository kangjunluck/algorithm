# 어려운걸~ 못풀었으
import sys


input = sys.stdin.readline

h = 19
board = []
for _ in range(h):
    board.append(list(map(int,input().split())))
visited = [[0 for __ in range(h)] for ___ in range(h)]


dc = [1, 1, 1, -1, -1, -1, 0, 0]
dr = [1, 0, -1, 1, 0, -1, -1, 1]

def dfs(i, j, color, std = 0, cnt = 0):
    print(i, j, std, cnt)
    if cnt == 4:
        if std == 'ru':
            nextC = i +dc[0]
            nextR = j +dr[0]
            if 0<=nextC<h and 0<=nextR<h and visited[nextC][nextR] == 0 and board[nextC][nextR] == color:
                return False
            else:
                return True
        elif std == 'u':
            nextC = i +dc[1]
            nextR = j +dr[1]
            if 0<=nextC<h and 0<=nextR<h and visited[nextC][nextR] == 0 and board[nextC][nextR] == color:
                return False
            else:
                return True
        elif std == 'lu':
            nextC = i +dc[2]
            nextR = j +dr[2]
            if 0<=nextC<h and 0<=nextR<h and visited[nextC][nextR] == 0 and board[nextC][nextR] == color:
                return False
            else:
                return True
        elif std == 'rd':
            nextC = i +dc[3]
            nextR = j +dr[3]
            if 0<=nextC<h and 0<=nextR<h and visited[nextC][nextR] == 0 and board[nextC][nextR] == color:
                return False
            else:
                return True
        elif std == 'd':
            nextC = i +dc[4]
            nextR = j +dr[4]
            if 0<=nextC<h and 0<=nextR<h and visited[nextC][nextR] == 0 and board[nextC][nextR] == color:
                return False
            else:
                return True
        elif std == 'ld':
            nextC = i +dc[5]
            nextR = j +dr[5]
            if 0<=nextC<h and 0<=nextR<h and visited[nextC][nextR] == 0 and board[nextC][nextR] == color:
                return False
            else:
                return True
        elif std == 'l':
            nextC = i +dc[6]
            nextR = j +dr[6]
            if 0<=nextC<h and 0<=nextR<h and visited[nextC][nextR] == 0 and board[nextC][nextR] == color:
                return False
            else:
                return True
        elif std == 'r':
            nextC = i +dc[7]
            nextR = j +dr[7]
            if 0<=nextC<h and 0<=nextR<h and visited[nextC][nextR] == 0 and board[nextC][nextR] == color:
                return False
            else:
                return True
    if std == 0:
        for step in range(8):
            nextC = i + dc[step]
            nextR = j + dr[step]
            if 0<=nextC<h and 0<=nextR<h and visited[nextC][nextR] == 0 and board[nextC][nextR] == color:
                
                if step == 0:
                    if dfs(nextC, nextR, color, std ='ru', cnt = cnt+1):
                        set_list.append((nextC, nextR))
                        return True
                elif step == 1:
                    if dfs(nextC, nextR, color, std ='u', cnt = cnt+1):
                        set_list.append((nextC, nextR))
                        return True
                elif step == 2:
                    if dfs(nextC, nextR, color, std ='lu', cnt = cnt+1):
                        set_list.append((nextC, nextR))
                        return True
                elif step == 3:
                    if dfs(nextC, nextR, color, std ='rd', cnt = cnt+1):
                        set_list.append((nextC, nextR))
                        return True
                elif step == 4:
                    if dfs(nextC, nextR, color, std ='d', cnt = cnt+1):
                        set_list.append((nextC, nextR))
                        return True
                elif step == 5:
                    if dfs(nextC, nextR, color, std ='ld', cnt = cnt+1):
                        set_list.append((nextC, nextR))
                        return True
                elif step == 6:
                    if dfs(nextC, nextR, color, std ='l', cnt = cnt+1):
                        set_list.append((nextC, nextR))
                        return True
                elif step == 7:
                    if dfs(nextC, nextR, color, std ='r', cnt = cnt+1):
                        set_list.append((nextC, nextR))
                        return True
    elif std == 'ru':
        nextC = i +dc[0]
        nextR = j +dr[0]
        if 0<=nextC<h and 0<=nextR<h and visited[nextC][nextR] == 0 and board[nextC][nextR] == color:
            if dfs(nextC, nextR, color, std ='ru', cnt = cnt+1):
                        set_list.append((nextC, nextR))
                        return True

    elif std == 'u':
        nextC = i +dc[1]
        nextR = j +dr[1]
        if 0<=nextC<h and 0<=nextR<h and visited[nextC][nextR] == 0 and board[nextC][nextR] == color:
            if dfs(nextC, nextR, color, std ='u', cnt = cnt+1):
                        set_list.append((nextC, nextR))
                        return True
    elif std == 'lu':
        nextC = i +dc[2]
        nextR = j +dr[2]
        if 0<=nextC<h and 0<=nextR<h and visited[nextC][nextR] == 0 and board[nextC][nextR] == color:
            if dfs(nextC, nextR, color, std ='lu', cnt = cnt+1):
                        set_list.append((nextC, nextR))
                        return True
    elif std == 'rd':
        nextC = i +dc[3]
        nextR = j +dr[3]
        if 0<=nextC<h and 0<=nextR<h and visited[nextC][nextR] == 0 and board[nextC][nextR] == color:
            if dfs(nextC, nextR, color, std ='rd', cnt = cnt+1):
                        set_list.append((nextC, nextR))
                        return True
    elif std == 'd':
        nextC = i +dc[4]
        nextR = j +dr[4]
        if 0<=nextC<h and 0<=nextR<h and visited[nextC][nextR] == 0 and board[nextC][nextR] == color:
            if dfs(nextC, nextR, color, std ='d', cnt = cnt+1):
                        set_list.append((nextC, nextR))
                        return True
    elif std == 'ld':
        nextC = i +dc[5]
        nextR = j +dr[5]
        if 0<=nextC<h and 0<=nextR<h and visited[nextC][nextR] == 0 and board[nextC][nextR] == color:
            if dfs(nextC, nextR, color, std ='ld', cnt = cnt+1):
                        set_list.append((nextC, nextR))
                        return True
    elif std == 'l':
        nextC = i +dc[6]
        nextR = j +dr[6]
        if 0<=nextC<h and 0<=nextR<h and visited[nextC][nextR] == 0 and board[nextC][nextR] == color:
            if dfs(nextC, nextR, color, std ='l', cnt = cnt+1):
                        set_list.append((nextC, nextR))
                        return True
    elif std == 'r':
        nextC = i +dc[7]
        nextR = j +dr[7]
        if 0<=nextC<h and 0<=nextR<h and visited[nextC][nextR] == 0 and board[nextC][nextR] == color:
            if dfs(nextC, nextR, color, std ='r', cnt = cnt+1):
                        set_list.append((nextC, nextR))
                        return True

start_list = []
for i in range(h):
    for j in range(h):
        if board[i][j] == 1:
            start_list.append((i,j,1))
        elif board[i][j] == 2:
            start_list.append((i,j,2))
ans = []
for part in start_list:
    set_list = []
    x, y, color = part[0], part[1], part[2]
    visited[x][y] = 1
    if dfs(x,y,color):
        set_list.append((x,y))
        sort_list = sorted(set_list, key= lambda x:(x[1],x[0]))
        ans.append(sort_list[0])
if ans:
    print(color)
    print(ans[0][0]+1, ans[0][1]+1)
else:
    print(0)