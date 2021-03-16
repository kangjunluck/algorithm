import sys

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    n = int(input())
    where = []
    for _ in range(n+2):
        a, b = map(int, input().split())
        where.append((a, b))
    visited = [0 for _ in range(n+2)]
    start = where[0]
    end = where[n+1]
    q = [(0, start[0], start[1])]
    visited[0] = 1
    isCan = False
    while q:
        now = q.pop(0)
        if now[0] == n+1:
            isCan = True
            break
        for i in range(n+2):
            need = (abs(where[i][0] - now[1]) +  abs(where[i][1] - now[2])) // 50
            if (abs(where[i][0] - now[1]) +  abs(where[i][1] - now[2])) % 50:
                need += 1
            if visited[i]: continue
            if need > 20: continue 
            visited[i] = 1
            q.append((i, where[i][0], where[i][1]))
    if isCan:
        print('happy')
    else:
        print('sad')
