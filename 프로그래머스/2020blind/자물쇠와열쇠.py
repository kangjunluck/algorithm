def solution(key, lock):
    answer = False
    n = len(key)
    m = len(lock)
    
    hom = []
    str = 0
    for i in range(m):
        for j in range(m):
            if lock[i][j] == 0:
                if str:
                    hom.append((str[0] - i, str[1] - j))
                else:
                    str = (i, j)

    cnt = 0
    isEnd = False
    while cnt <= 3:
        ke = []
        for i in range(n):
            for j in range(n):
                if key[i][j] == 1:
                    ke.append((i, j))
        # 하나씩 꺼내 hom의 하나씩 매칭시킨다.
        for i in range(len(ke)):
            str_key = ke[i]
            isTrue = True
            for j in range(len(hom)):
                addx, addy = hom[j]
                nextR = str_key[0] + addx
                nextC = str_key[1] + addy
                if (nextR, nextC) in ke:
                    continue
                else:
                    isTrue = False
                    break
            if isTrue:
                answer = True
                isEnd = True
                break
            
        # key 회전시키기
        tmp = key
        key = [[0 for _ in range(n)] for _ in range(n)]
        for r in range(n):
            for c in range(n):
                key[c][n-1-r] = tmp[r][c]
        if isEnd:
            break
        cnt += 1
        
    return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))