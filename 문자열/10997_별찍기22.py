import sys

input = sys.stdin.readline

n  = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

if n == 1:
    print('*')
else:
    board = [[' ' for _ in range(4*n-3)] for _ in range(4*n-1)]
    sr, sc = (4*n-1)//2 + 1, (4*n-3)//2
    board[sr][sc] = '*'
    length = 2
    cnt = 1
    while cnt < n:
        for ar in range(0,4,2):
            for aa in range(length):
                sr = sr + dr[ar]
                sc = sc + dc[ar]
                board[sr][sc] = '*'
        length += 2
        for ar in range(1,4,2):
            for bb in range(length):
                sr = sr + dr[ar]
                sc = sc + dc[ar]
                board[sr][sc] = '*'
        length += 2
        cnt += 1
    for cc in range(length):
        sr = sr + dr[0]
        sc = sc + dc[0]
        board[sr][sc] = '*'
    for dd in range(length-2):
        sr = sr + dr[2]
        sc = sc + dc[2]
        board[sr][sc] = '*'
    for k in range(1, 4*n-3):
        board[1][k] =''
    for part in board:
        print(''.join(part))