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
    # key 돌리는 방법?
    cnt = 0
    isEnd = False
    while hom and cnt <= 3:
        ke = []
        for i in range(n):
            for j in range(n):
                if key[i][j] == 1:
                    ke.append((i, j))
        # 하나씩 꺼내 hom의 하나씩 매칭시킨다.
        check = [0 for _ in range(len(ke))]
        for i in range(len(ke)):
            check[i] = 1
            str_key = ke[i]
            isTrue = True
            hom_cnt = 1
            for j in range(len(ke)):
                if check[j]: continue
                nextR = ke[j][0]
                nextC = ke[j][1]
                gapR = str_key[0] - nextR
                gapC = str_key[1] - nextC
                if 0 <= str[0] - gapR < m and 0 <= str[1] - gapC < m:
                    if (gapR, gapC) in hom:
                        hom_cnt += 1
                        continue
                    else:
                        isTrue = False
                        break
            if isTrue and hom_cnt == (len(hom)+1):
                answer = True
                isEnd = True
                break
            check[i] = 0
            
        # key 회전시키기
        tmp = key
        key = [[0 for _ in range(n)] for _ in range(n)]
        for r in range(n):
            for c in range(n):
                key[c][n-1-r] = tmp[r][c]
        if isEnd:
            break
        cnt += 1
        
    if not hom:
        answer = True
        
    return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

print(solution(key, lock))