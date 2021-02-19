import sys

input = sys.stdin.readline

n, m, k = map(int,input().split())

board = [0] * n # 받은 갯수 저장 위치
cnt = 0 # 공 던진 수
idx = 0 # 0 ~ 4까지 왓다 갓다
board[idx] = 1
while True:
    if board[idx] & 1:
        idx = idx + k
        if idx >= n:
            idx = idx - n
        board[idx] += 1
        cnt += 1
    else:
        idx = idx - k
        if idx < 0:
            idx = idx + n
        board[idx] += 1
        cnt += 1
    if board[idx] == m:
        break
print(cnt)