n = int(input())

map = [list(map(int, input().split())) for _ in range(n)]
route = [[(0, 1), (1, 1)], [(0, 1),(1, 1), (1, 0)], [(1, 1), (1, 0)]]
answer = 0

# visited = 3차 행렬로 dp하듯이 저장

def dfs(a, b, c):
    global answer
    if a == n-1 and b == n-1:
        answer += 1
        return
    for ro in route[c]:
        nr = a + ro[0]
        nc = b + ro[1]
        if ro == (1, 1):
            if 0<=nr<n and 0<=nc<n and map[nr][nc] == 0 and map[nr][nc-1] == 0 and map[nr-1][nc] == 0:
                dfs(nr, nc, 1)
        else:
            if 0<=nr<n and 0<=nc<n and map[nr][nc] == 0:
                if ro == (0, 1):
                    dfs(nr, nc, 0)
                else:
                    dfs(nr, nc, 2)

dfs(0, 1, 0)
print(answer)