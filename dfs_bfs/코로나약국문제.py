import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(n)]

que = deque()
que.append((0,0,k,0)) # (r, c, k, bit)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 해당 위치에서 들고있을 수 있는 마스크의 최대 개수
visit = [[-1 for _ in range(m)] for _ in range(n)]

while que:

    r, c, cnt, bit = que.popleft()
    if visit[r][c] <= cnt:
        visit[r][c] = cnt
        if r==n-1 and c==m-1:  # 도착지점에 왔다면 continue
            continue
        
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0<=nr<n and 0<=nc<m:
                if city[nr][nc]:  # 다음 위치가 약국일 때
                    b = nr*m+nc  # 지도상 약국 위치에 번호 매기기
                    if bit & (1<<b):  # 방문한 약국인 경우
                        que.append((nr, nc, cnt-1, bit))
                    else:  # 방문한적 없는 약국인 경우
                        que.append((nr, nc, cnt+city[nr][nc]-1, bit|(1<<b)))
                else:  # 다음 위치가 약국이 아닐 때
                    que.append((nr, nc, cnt-1, bit))

print(visit[n-1][m-1])