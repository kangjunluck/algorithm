from collections import deque

n = int(input())
board = [[0]*n for _ in range(n)]
k = int(input())
for _ in range(k):
    a, b = map(int,input().split())
    board[a-1][b-1] = 1
board[0][0] = 2
head = (0, 0)

q = deque()
q.append((0, 0))
board[0][0] = 2
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
way = 0 ## 0 우, 1 하, 2 좌, 3, 상
l = int(input())
times = deque()
for _ in range(l):
    ss, cc = map(str,input().split())
    times.append((int(ss), cc))
time = 0
isEnd = False
while times:
    s, c = times.popleft()
    if isEnd: continue
    while s > time:
        ## 머리
        time += 1
        hr = head[0] + dr[way]
        hc = head[1] + dc[way]
        if 0<=hr<n and 0<=hc<n and board[hr][hc] != 2:
            if board[hr][hc] == 1:
                board[hr][hc] = 2
                q.append((hr, hc))
            else:
                board[hr][hc] = 2
                q.append((hr, hc))
                tr, tc = q.popleft()
                board[tr][tc] = 0
        else:
            isEnd = True
            break
        head = (hr, hc)
    if c == 'D':
        way = (way + 1)%4
    else:
        way = (way - 1)%4

while isEnd == False:
    time += 1
    hr = head[0] + dr[way]
    hc = head[1] + dc[way]
    if 0<=hr<n and 0<=hc<n and board[hr][hc] != 2:
        if board[hr][hc] == 1:
            board[hr][hc] = 2
            q.append((hr, hc))
        else:
            board[hr][hc] = 2
            q.append((hr, hc))
            tr, tc = q.popleft()
            board[tr][tc] = 0
    else:
        break
    head = (hr, hc)
print(time)

