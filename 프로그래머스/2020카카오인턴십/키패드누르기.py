def solution(numbers, hand):
    answer = ''
    info = {
        0:(3,1),
        1:(0,0),
        2:(0,1),
        3:(0,2),
        4:(1,0),
        5:(1,1),
        6:(1,2),
        7:(2,0),
        8:(2,1),
        9:(2,2),        
    }
    ls = (3, 0)
    rs = (3, 2)
    
    for number in numbers:
        # 1,4,7 일때 왼손만
        if number == 1 or number == 4 or number == 7:
            ls = info[number]
            answer += 'L'
            continue
        # 3,6,9 일때 오른손만
        elif number == 3 or number == 6 or number == 9:
            rs = info[number]
            answer += 'R'
            continue
        else:
            na, nb = info[number]
            length_l = abs(na - ls[0]) + abs(nb - ls[1])
            length_r = abs(na - rs[0]) + abs(nb - rs[1])
            if length_l > length_r:
                answer += 'R'
                rs = info[number]
            elif length_l < length_r:
                answer += 'L'
                ls = info[number]
            else:
                if hand == 'right':
                    answer += 'R'
                    rs = info[number]
                else:
                    answer += 'L'
                    ls = info[number]
        
        
    return answer