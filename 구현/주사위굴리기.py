from collections import deque

n, m, x, y, k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
steps = list(map(int,input().split()))
steps = deque(steps)

dice = [0]*7 ## 위치는 문제에 있는 순서대로

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


while steps:
    way = steps.popleft() - 1
    nx = x + dr[way]
    ny = y + dc[way]
    if 0<=nx<n and 0<=ny<m:
        if way == 0:
            dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
        elif way == 1:
            dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
        elif way == 2:
            dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
        else:
            dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]

        if board[nx][ny] ==0:
            board[nx][ny] = dice[1]
        else:
            dice[1] = board[nx][ny]
            board[nx][ny] = 0
        print(dice[6])
        x = nx
        y = ny

    

