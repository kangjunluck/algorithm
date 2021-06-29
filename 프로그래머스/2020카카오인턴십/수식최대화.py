import copy
answer = 0
def solution(expression):
    
    standard = ['+', '-', '*']
    # 완전탐색
    cal = []
    numbers = []
    num = ''
    for i in range(len(expression)):
        a = expression[i]
        if a in standard:
            cal.append(a)
            numbers.append(int(num))
            num = ''
        else:
            num += a
    numbers.append(int(num))
    now_cal = list(set(cal))
    n = len(now_cal)
    check = [0 for _ in range(n)]
    sel = [0 for _ in range(n)]
    def permu(idx):
        global answer
        if idx == n:
            cal_tmp = copy.deepcopy(cal)
            numbers_tmp = copy.deepcopy(numbers)
            for step in sel:
                while step in cal_tmp:
                    idx = cal_tmp.index(step)
                    if step == '+':
                        numbers_tmp[idx] = numbers_tmp[idx] + numbers_tmp[idx+1]
                    elif step == '-':
                        numbers_tmp[idx] = numbers_tmp[idx] - numbers_tmp[idx+1]
                    else:
                        numbers_tmp[idx] = numbers_tmp[idx] * numbers_tmp[idx+1]
                    cal_tmp.remove(step)
                    del numbers_tmp[idx+1]
            if answer < abs(numbers_tmp[0]):
                answer = abs(numbers_tmp[0])
            return
        
        for i in range(n):
            if check[i]: continue
            check[i] = 1
            sel[idx] = now_cal[i]
            permu(idx+1)
            check[i] = 0
    permu(0)
    return answer