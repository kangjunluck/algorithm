import sys

input = sys.stdin.readline

h = 19
board = []
for _ in range(h):
    board.append(list(map(int,input().split())))

dc = [1, 1, 1, 0, 0, -1, -1, -1]
dr = [1, 0, -1, 1, -1, 1, 0, -1]
result = []
who = 0
for i in range(h):
    for j in range(h):
        if board[i][j] == 1:
            for k in range(8):
                a, b = i, j
                cnt = 1
                group = []
                group.append((a, b))
                nextR = a + dc[k]
                nextC = b + dr[k]
                if 0 <= nextR < h and 0 <= nextC < h and board[nextR][nextC] == 1:
                    while 0 <= nextR < h and 0 <= nextC < h and board[nextR][nextC] == 1:
                        group.append((nextR, nextC))
                        cnt += 1
                        nextR += dc[k]
                        nextC += dr[k]
                a, b = i, j
                nextR = a + dc[7-k]
                nextC = b + dr[7-k]
                if 0 <= nextR < h and 0 <= nextC < h and board[nextR][nextC] == 1:
                    while 0 <= nextR < h and 0 <= nextC < h and board[nextR][nextC] == 1:
                        group.append((nextR, nextC))
                        cnt += 1
                        nextR += dc[7-k]
                        nextC += dr[7-k]
                if cnt == 5:
                    who = 1
                    result.append(group)
        elif board[i][j] == 2:
            for k in range(8):
                a, b = i, j
                cnt = 0
                group = []
                group.append((a, b))
                nextR = a + dc[k]
                nextC = b + dr[k]
                if 0 <= nextR < h and 0 <= nextC < h and board[nextR][nextC] == 2:
                    while 0 <= nextR < h and 0 <= nextC < h and board[nextR][nextC] == 2:
                        group.append((nextR, nextC))
                        cnt += 1
                        nextR += dc[k]
                        nextC += dr[k]
                a, b = i, j
                nextR = a + dc[7-k]
                nextC = b + dr[7-k]
                if 0 <= nextR < h and 0 <= nextC < h and board[nextR][nextC] == 2:
                    while 0 <= nextR < h and 0 <= nextC < h and board[nextR][nextC] == 2:
                        group.append((nextR, nextC))
                        cnt += 1
                        nextR += dc[7-k]
                        nextC += dr[7-k]
                if cnt == 5:
                    who = 2
                    result.append(group)
                    
if result:
    sort_list = sorted(result[0], key= lambda x:x[1])
    print(who)
    print(sort_list[0][0]+1, sort_list[0][1]+1)

else:
    print(who)