import sys

input = sys.stdin.readline

h = 19
board = []
for _ in range(h):
    board.append(list(map(int,input().split())))

def rightleft(a, b, color):
    std = 1
    i, j = a, b
    if j + 1 < h and board[i][j + 1] == color:
        while j + 1 < h and board[i][j + 1] == color:
            std += 1
            j += 1
    i, j = a, b
    if j > 0 and board[i][j - 1] == color:
        while j > 0 and board[i][j - 1] == color:
            std += 1
            j -= 1
    if std == 5:
        return 1
    else:
        return 0

def updown(a, b, color):
    std = 1
    i, j = a, b
    if i + 1 < h and board[i + 1][j] == color:
        while i + 1 < h and board[i + 1][j] == color:
            std += 1
            i += 1
    i, j = a, b
    if i > 0 and board[i - 1][j] == color:
        while i > 0 and board[i - 1][j] == color:
            std += 1
            i -= 1
    if std == 5:
        return 1
    else:
        return 0

def upleft(a, b, color):
    std = 1
    i, j = a, b
    if i + 1 < h and j + 1 < h and board[i + 1][j + 1] == color:
        while i + 1 < h and j + 1 < h  and board[i + 1][j + 1] == color:
            std += 1
            i += 1
            j += 1
    i, j = a, b
    if i > 0 and j > 0 and board[i - 1][j - 1] == color:
        while i > 0 and j > 0 and board[i - 1][j - 1] == color:
            std += 1
            i -= 1
            j -= 1
    if std == 5:
        return 1
    else:
        return 0

def upright(a, b, color):
    std = 1
    i, j = a, b
    if i + 1 < h and j > 0 and board[i + 1][j - 1] == color:
        while i + 1 < h and j > 0 and board[i + 1][j + 1] == color:
            std += 1
            i += 1
            j -= 1
    i, j = a, b
    if i > 0 and j + 1 < h and board[i - 1][j + 1] == color:
        while i > 0 and j + 1 < h and board[i - 1][j + 1] == color:
            std += 1
            i -= 1
            j += 1
    if std == 5:
        return 1
    else:
        return 0
ans = 0
dot_list = []
for m in range(h):
    if len(dot_list) == 5:
        break
    else:
        for n in range(h):
            cnt = 0
            if board[m][n] == 1:
                cnt += rightleft(m, n, 1)
                cnt += updown(m, n, 1)
                cnt += upright(m, n, 1)
                cnt += upleft(m, n, 1)
                if cnt != 0:
                    ans = 1
                    dot_list.append((m, n))
                    break
            elif board[m][n] == 2:
                cnt += rightleft(m, n, 2)
                cnt += updown(m, n, 2)
                cnt += upright(m, n, 2)
                cnt += upleft(m, n, 2)
                if cnt != 0:
                    ans = 2
                    dot_list.append((m, n))
                    break

if dot_list:
    dot_list = sorted(dot_list, key = lambda x:x[1])
    print(ans)
    print(dot_list[0][0]+1, dot_list[0][1]+1)
else:
    print(0)