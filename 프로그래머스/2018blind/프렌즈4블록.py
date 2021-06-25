# 천천히

def solution(m, n, board):
    answer = 0
    data = []
    for bo in board:
        data.append(list(map(str, bo.strip())))
        
    def isFour(i, j):
        if data[i][j] == data[i+1][j] == data[i][j+1] == data[i+1][j+1]:
            return True
        return False
    def down():
        for j in range(n):
            for i in range(m-2, -1, -1):
                while i <= m-2 and data[i][j] != '' and data[i+1][j] == '':
                    data[i][j], data[i+1][j] = data[i+1][j], data[i][j]
                    i += 1                    
    while True:
        change = []
        for i in range(m-1):
            for j in range(n-1):
                if data[i][j] == '': continue
                if isFour(i, j):
                    change.append((i, j))
                    change.append((i, j+1))
                    change.append((i+1, j))
                    change.append((i+1, j+1))
        change = set(change)
        cnt = len(change)
        if cnt == 0:
            break
        answer += len(change)
        for a, b in change:
            data[a][b] = ''
        down()

    return answer