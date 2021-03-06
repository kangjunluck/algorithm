import sys

input = sys.stdin.readline

n = int(input())

board = [list(map(str, input().split())) for _ in range(n)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def gets(a, b):
    isOkay = True
    for i in range(4):
        if isOkay == False: break
        nextR = a + dr[i]
        nextC = b + dc[i]
        while 0<=nextR<n and 0<=nextC<n:
            if board[nextR][nextC] == 'O':
                break
            elif board[nextR][nextC] == 'S':
                isOkay = False
                break
            nextR += dr[i]
            nextC += dc[i]
        
    return isOkay

teachers = []
nothing = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
        elif board[i][j] == 'X':
            nothing .append((i, j))
isanswer = False
for x in range(len(nothing)-2):
    if isanswer: break
    board[nothing[x][0]][nothing[x][1]] = 'O'
    for y in range(x+1, len(nothing)-1):
        if isanswer: break
        board[nothing[y][0]][nothing[y][1]] = 'O'
        for z in range(y+1, len(nothing)):
            if isanswer: break
            board[nothing[z][0]][nothing[z][1]] = 'O'

            allTrue = True
            for teacher in teachers:
                a, b = teacher[0], teacher[1]
                if gets(a, b) == False:
                    allTrue = False
                    break
            if allTrue:
                isanswer = True

            board[nothing[z][0]][nothing[z][1]] = 'X'
        board[nothing[y][0]][nothing[y][1]] = 'X'
    board[nothing[x][0]][nothing[x][1]] = 'X'

if isanswer: print('YES')
else: print('NO')