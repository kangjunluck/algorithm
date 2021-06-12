def solution(info, query):
    answer = []
    reinfo = []
    for person in info:
        reinfo.append(list(map(str, person.split())))
    
    for step in query:
        datas = step.split()
        datas = [x for x in datas if x != 'and']
        n = len(datas)
        cnt = 0
        for rein in reinfo:
            isTrue = True
            for i in range(n):
                if datas[i] == '-':
                    continue
                if i == n-1:
                    if int(datas[i]) > int(rein[i]):
                        isTrue = False
                        break
                    else:
                        continue
                if datas[i] != rein[i]:
                    isTrue = False
                    break
            if isTrue: cnt += 1
        answer.append(cnt) 
    
    return answer