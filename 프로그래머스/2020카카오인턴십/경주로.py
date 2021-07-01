dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
# 0, 1, 2, 3 우 하 좌 상
answer = 10000000

def solution(board):
    global answer
    n = len(board)
    
    def dfs(a, b, way, total=0):
        global answer
        # 남은 길이
        h = n-1 - a 
        w = n-1 - b
        rest = h + w
        if h != 0 and w != 0:
            rest += 5
        if total + rest > answer:
            return
        if a == n-1 and b == n-1:
            answer = total
            return
        
        for i in range(4):
            if abs(way-i) == 2: continue
            nextR = a + dr[i]
            nextC = b + dc[i]
            if 0<=nextR<n and 0<=nextC<n and board[nextR][nextC] == 0 and visited[nextR][nextC] == 0:
                visited[nextR][nextC] = 1
                cost = 6
                if way-i == 0: cost = 1
                dfs(nextR, nextC, i, total+cost)
                visited[nextR][nextC] = 0
    visited = [[0]*n for _ in range(n)]

    dfs(0, 0, 0)
    dfs(0, 0, 1)
            
    answer *= 100
        
    return answer