def solution(s):
    answer = 0
    n = len(s)
    
    if n == 1:
        answer = 1
    else:
        mini = 10000
        for unit in range(1, n//2+1):
            re_s = ''

            before = ''
            num = 0
            part = ''
            for i in range(n):
                part += s[i]
                if len(part) == unit:
                    if part == before:
                        num += 1
                    else:
                        if num > 1:
                            re_s += str(num)
                            re_s += before
                        elif num == 1:
                            re_s += before                        
                        num = 1
                        before = part
                    part = ''
            if num > 1:
                re_s += str(num)
                re_s += before
            elif num == 1:
                re_s += before
            re_s += part

            m = len(re_s)
            mini = min(m, mini)

        answer = mini                
        
    return answer