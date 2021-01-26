#bfs로 풀어보기

import sys
import copy

from collections import deque

sys.stdin = open('10026.txt', 'r')
input = sys.stdin.readline

n = int(input())

board = []
for _ in range(n):
    board.append(list(map(str, input().strip()))) ## strip으로 해야 문자가 나뉜다 조각조각!

q = deque()

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for _ in range(2):
    ans=0
    visited = [[0 for __ in range(n)] for ___ in range(n)]
    for x in range(n):
        for y in range(n):
            if visited[y][x]==0:
                ans += 1
                visited[y][x] = 1
                q.append((y, x, board[y][x]))
                while q:
                    now = q.popleft()               
                    if now[2]=='G':
                        board[now[0]][now[1]]='R'

                    for arrow in range(4):
                        nextC = now[0] + dc[arrow]
                        nextR = now[1] + dr[arrow]

                        if 0<=nextC<n and 0<=nextR<n and visited[nextC][nextR] ==0 and board[nextC][nextR] == now[2]:
                            visited[nextC][nextR] = 1
                            q.append((nextC, nextR, now[2]))

    print(ans, end=' ')