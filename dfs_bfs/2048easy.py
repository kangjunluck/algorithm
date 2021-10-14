## 1024경우이므로 다 해도 될 듯하다.
n = int(input())
board = [[-1] + list(map(int,input().split())) + [-1] for _ in range(n)]
board = [[-1]*(n+2)] + board + [[-1] * (n+2)]


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def move(board, ar):

    return board

def makeAns(idx, board):

    for ar in range(4):
        makeAns(idx+1, move(board, ar))