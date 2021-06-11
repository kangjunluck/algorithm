def solution(new_id):
    answer = ''
    # 한번 훝을 때 이상한거 있나 확인해주기 + 대문자 소문자 변환
    n = len(new_id)
    expt = ['-', '_', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    step1 = ''
    i = 0
    while i < n:
        if 65 <= ord(new_id[i]) <= 90:
            step1 += chr(ord(new_id[i]) + 32)
            i += 1 
            continue
        elif 97 <= ord(new_id[i]) <= 122:
            step1 += new_id[i]
            i += 1
            continue
        
        if new_id[i] in expt:
            step1 += new_id[i]
            i += 1
            continue
        
        if new_id[i] == '.':
            if step1:
                if step1[-1] == '.':
                    i += 1
                    continue
                else:
                    step1 += '.'
                    i += 1
                    continue
            else:
                i += 1
                continue
        i += 1
    length = len(step1)
    if length != 0:
        if step1[-1] == '.':
            step1 = step1[:length-1]
    # 길이, '.' 여부 계속 확인
    
    while True:
        length = len(step1)
        if length == 0:
            step1 = 'a'
        elif 0 < length <= 2:
            step1 += step1[-1]
        elif length >= 16:
            step1 = step1[:15]
        else:
            if step1[-1] == '.':
                step1 = step1[:length-1]
            else:
                break
    answer = step1        

    return answer

new_id = "=.="

solution(new_id)