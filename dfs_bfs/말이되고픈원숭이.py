from collections import deque

k = int(input())
n, m = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(m)]

q = deque()
q.append((0, 0, k, 0))

dr = [1, -1, 0, 0]
drx = [-2, -2, -1, -1, 1, 1, 2, 2]
dc = [0, 0, 1, -1]
dcx = [1, -1, 2, -2, 2, -2, 1, -1]
answer = 0
while q:
    na, nb, cnt, time = q.popleft()
    if na == m-1 and nb == n-1:
        answer = time
        break
    for ar in range(4):
        nexta = na+dr[ar]
        nextb = nb+dc[ar]
        if 0<=nexta<m and 0<=nextb<n and board[nexta][nextb] ==0:
            q.append((nexta, nextb, cnt, time+1))
    if cnt > 0:
        for arr in range(8):
            nexta = na+drx[arr]
            nextb = nb+dcx[arr]
            if 0<=nexta<m and 0<=nextb<n and board[nexta][nextb] ==0:
                q.append((nexta, nextb, cnt-1, time+1))

print(answer)
