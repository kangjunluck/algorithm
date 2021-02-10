import sys


input = sys.stdin.readline

h = 19
board = []
for _ in range(h):
    board.append(list(map(int,input().split())))
visited = [[0 for __ in range(h)] for ___ in range(h)]

start_list = []
for i in range(h):
    for j in range(h):
        if board[i][j] == 1:
            start_list.append((i,j,1))
        elif board[i][j] == 2:
            start_list.append((i,j,2))
dc = [1, 1, 1, -1, -1, -1, 0, 0]
dr = [1, 0, -1, 1, 0, -1, -1, 1]
def dfs(index, i, j, color):
    set_list.append((i,j,color))
    nextC = i + dc[index]
    nextR = j + dr[index]
    if 0<=nextC<h and 0<=nextR<h and board[nextC][nextR] == color:
        dfs(index, nextC, nextR, color)
result = []
for part in start_list:
    box = []
    x, y, color = part[0], part[1], part[2]
    for array in range(8):
        set_list = []
        dfs(array, x, y, color)
        print(set_list)
        if len(set_list) == 5:
            box.append(set_list)
    if box:
        result.append(box[0])
print(result)
if result:
    ans = result[0]
    ans2 = sorted(ans, key = lambda x:(x[1], x[0]))
    print(ans2[0][2])
    print(ans2[0][0]+1, ans2[0][1]+1)
else:
    print(0)