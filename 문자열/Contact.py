T = int(input())
for tc in range(1,T+1):
    data = input()
    n = len(data)
    answer = 'NO'
    

# 한칸씩 확인, 갯수들을 다 파악해보자. 1경우인지, 2경우인지, 다끝낫는지로 나누어 보자
def check(i, case, zero):
    global answer
    if i == n:
        if case == 0:
            answer = 'YES'
        return
    if case == 0:
        if data[i] == '1':
            check(i+1, 1, 1)
        else:
            check(i+1, 2)

    elif case == 1:
        if zero == 0:
            if data[i] == '0':
                check(i+1, 1, 1)
        elif zero == 1:
            if data[i] == '0':
                check(i+1, 1, 2)
        else:
            if data[i] == '0':
                check(i+1, 1, 3)
            else:
                check(i+1, 0, 0)
                check(i+1, 1, 0)


        



    else:
        if i+1 < n and data[i+1] == '1':
            check(i+1, 0)
        else:
            return


