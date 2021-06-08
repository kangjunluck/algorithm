def solution(rows, columns, queries):
    answer = []
    
    # board 만들기
    board = []
    for i in range(rows):
        stand = columns * i
        part = []
        for j in range(columns):
            part.append(stand + j + 1)
        board.append(part)
        
    dr = [0, 1, 0, -1]    
    dc = [1, 0, -1, 0]
    
    for step in queries:
        y1, x1, y2, x2 = step
        width = abs(x2 - x1)
        height = abs(y2 - y1)
        # 4방향 돌기
        start = (y1-1, x1-1)
        s = [board[y1-1][x1-1]]
        mini = 1000000
        for ar in range(4):
            if ar%2:
                length = height
            else:
                length = width
            while length > 0:
                before = s.pop()
                if before < mini:
                    mini = before
                nextR = start[0] + dr[ar]
                nextC = start[1] + dc[ar]
                start = (nextR, nextC)
                s.append(board[nextR][nextC])
                board[nextR][nextC] = before
                length -= 1
        answer.append(mini)
    return answer