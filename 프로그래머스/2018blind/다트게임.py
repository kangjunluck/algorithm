def solution(dartResult):
    answer = 0
    n = len(dartResult)
    nums = [ str(i) for i in range(10) ]
    cal = []
    
    i = 0
    while i <= n-1:
        if dartResult[i] == '1':
            # 10 인지 1 인지
            if dartResult[i+1] == '0':
                # 10인 경우
                cal.append(10)
                i += 2
            else:
                # 1인경우
                cal.append(1)
                i += 1
            continue
        elif dartResult[i] in nums:
            cal.append(int(dartResult[i]))
        elif dartResult[i] == 'S':
            cal[-1] **= 1
        elif dartResult[i] == 'D':
            cal[-1] **= 2
        elif dartResult[i] == 'T':
            cal[-1] **= 3
        elif dartResult[i] == '*':
            cal[-1] *= 2
            if len(cal) >= 2:
                cal[-2] *= 2
        elif dartResult[i] == '#':
            cal[-1] *= (-1)
        i += 1
    answer = sum(cal)
    return answer

# 문자열을 한번 탐색하며 새로운 리스트를 만든다.
# python이라 -1인덱스를 활용했지만 인덱스를 나타내는 변수를 정해서 진행하면 더 빠를 것으로 예상된다.