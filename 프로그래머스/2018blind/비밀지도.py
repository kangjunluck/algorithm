def solution(n, arr1, arr2):
    answer = []
    board = [[' ' for _ in range(n)] for _ in range(n)]
    
    def makebinary(num):
        bin = ''
        while num > 1:
            bin += str(num % 2)
            num = num // 2
        bin += str(num)
        while len(bin) < n:
            bin += '0'
        bin = bin[::-1]
        return bin
    
    def fillboard(arr):
        i = 0
        for num in arr:
            bin_num = makebinary(num)
            for j in range(n):
                if bin_num[j]  == '1' and board[i][j] == ' ':
                    board[i][j] = '#'
            i += 1
    fillboard(arr1)
    fillboard(arr2)
    for step in board:
        answer.append(''.join(step))
    
    return answer