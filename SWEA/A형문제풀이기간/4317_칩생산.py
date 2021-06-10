T = int(input())

for tc in range(1,T+1):
    h, w = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(h)]
    #완전탐색?
    cnt = 0
    def findans(i, j):
        global cnt
        if board[i][j] == 0 and board[i][j+1] == 0 and board[i+1][j+1] == 0 and board[i+1][j] == 0:
            board[i][j] = 1
            board[i][j+1] = 1
            board[i+1][j] = 1
            board[i+1][j+1] = 1
            cnt += 1
            findans(a+2, b)
            cnt -= 1
            board[i][j] = 0
            board[i][j+1] = 0
            board[i+1][j] = 0
            board[i+1][j+1] = 0
    findans(board)
    print(cnt)







