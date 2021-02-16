import sys

input = sys.stdin.readline

n = int(input()) #색종이 갯수

board = [ [0 for _ in range(101)] for __ in range(101)]

cnt = [0 for ___ in range(n)]

for paper in range(1, n+1):
    i, j, height, width = map(int, input().split())
    for a in range(height):
        for b in range(width):
            if board[i+a][j+b] == 0:
                board[i+a][j+b] = paper
                cnt[paper-1] += 1
            else:
                cnt[paper-1] += 1
                cnt[board[i+a][j+b]-1] -= 1
                board[i+a][j+b] = paper
for ans in cnt:
    print(ans)


