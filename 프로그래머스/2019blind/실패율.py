def solution(N, stages):
    answer = []
    total = [0 for _ in range(N+2)]
    noclear = [0 for _ in range(N+2)]
    for num in stages:
        noclear[num] += 1
        for i in range(1, num+1):
            total[i] += 1
    
    probability = [(i, noclear[i]/total[i]) if total[i] != 0 else (i, 0) for i in range(1,N+1)]
    
    proba = sorted(probability, key = lambda x:(-x[1], x[0]))
    
    for a, b in proba:
        answer.append(a)    
    
    return answer