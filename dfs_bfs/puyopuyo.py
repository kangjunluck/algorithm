import sys
from collections import deque

input = sys.stdin.readline

board = [list(map(str, input().strip())) for _ in range(12)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0

while True:
    for kk in range(12):
        print(board[kk])
    print('----------------------')
    # 다 돌아봤는데, 4개 이상 연결된 부분이 없다 면 break
    isClear = True
    visited = [[0]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.':
                if visited[i][j]: continue
                visited[i][j] = 1
                # 탐색 시작
                now = board[i][j]
                q = deque()
                q.append((i, j))
                cnt = 1
                while q:
                    x, y = q.popleft()
                    for ar in range(4):
                        nx = x + dx[ar]
                        ny = y + dy[ar]
                        if 0<=nx<12 and 0<=ny<6 and board[nx][ny] == now and visited[nx][ny] == 0:
                            q.append((nx, ny))
                            cnt += 1
                            visited[nx][ny] = 1
                if cnt < 4: continue
                isClear = False
                now = board[i][j]
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for ar in range(4):
                        nx = x + dx[ar]
                        ny = y + dy[ar]
                        if 0<=nx<12 and 0<=ny<6 and board[nx][ny] == now:
                            q.append((nx, ny))
                            board[nx][ny] = '.'
    if isClear: break
    answer += 1
    #  아래로 쭉 내리기
    for i in range(10, -1, -1):
        for j in range(5, -1, -1):
            ii = i
            jj = j
            while 0<=ii<11 and board[ii][jj] != '.' and board[ii+1][jj] == '.':
                board[ii][jj], board[ii+1][jj] = board[ii+1][jj], board[ii][jj]
                ii += 1

print(answer)
    

                
                

