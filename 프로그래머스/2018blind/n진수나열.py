def solution(n, t, m, p):
    answer = ''
    change = {
        0 : '0',
        1 : '1',
        2 : '2',
        3 : '3',
        4 : '4',
        5 : '5',
        6 : '6',
        7 : '7',
        8 : '8',
        9 : '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
        
    }
    def makebinary(a):
        bin = ''
        while a > n-1:
            waste = a%n
            bin += change[waste]
            a = a//n
        if a:
            bin += change[a]
        if bin == '':
            bin = '0'
        bin = bin[::-1]
        return bin
    num = 0
    line = ''
    while True:
        line += makebinary(num)
        if len(line) >= t*m:
            break
        num += 1
    j = 1
    idx = p-1
    while j <= t:
        answer += line[idx]
        idx += m
        j += 1
        

    return answer