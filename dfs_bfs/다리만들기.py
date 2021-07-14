from collections import deque
import copy

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

dr = [1, -1, 0 ,0]
dc = [0, 0, 1, -1]
land = 1
visited = [[0]*n for _ in range(n)]
lands = []
for i in range(n):
    for j in range(n):
        if visited[i][j] or board[i][j] == 0: continue

        one = deque()
        visited[i][j] = land
        q = deque()
        q.append((i, j))
        while q:
            a, b = q.popleft()
            one.append((a, b, 0))
            for ar in range(4):
                nexta = a + dr[ar]
                nextb = b + dc[ar]
                if 0<=nexta<n and 0<=nextb<n and board[nexta][nextb] == 1 and visited[nexta][nextb] == 0:
                    visited[nexta][nextb] = land
                    q.append((nexta, nextb))
        lands.append(one)
        land += 1
answer = 100000
landnum = 1
for part in lands:
    map = copy.deepcopy(visited)
    visit = [[0]*n for _ in range(n)]
    while part:
        aa, bb, cnt = part.popleft()
        if visited[aa][bb] != landnum and visited[aa][bb] != 0:
            answer = min(answer , cnt)
            break
        for ar in range(4):
            nextaa = aa + dr[ar]
            nextbb = bb + dc[ar]
            if 0<=nextaa<n and 0<=nextbb<n and visit[nextaa][nextbb] == 0 and visited[nextaa][nextbb] != landnum :
                visit[nextaa][nextbb] = 1
                part.append((nextaa, nextbb, cnt+1))

    landnum += 1
print(answer -1)
    
    



