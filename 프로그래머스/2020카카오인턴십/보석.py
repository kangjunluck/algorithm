# 이진탐색 풀이dd
def solution(gems):
    answer = []
    species = set(gems)
    n = len(gems)
    
    def check():
        part = set(gems[i:mid+1])
        if part == species: return True
        else : False
            
    mini = 100000
    for i in range(n):
        l = i
        r = n-1
        while l<r:
            mid = (l+r)//2
            if check(): r = mid
            else: l = mid + 1
        
        final = set(gems[i:r+1])
        if final == species:
            if r - i < mini:
                mini = r-i
                answer = [i+1, r+1]
    return answer


## dictionary로 풀기. 진짜 빠르다 dictionary가
def solution(gems):
    
    species = set(gems)
    n = len(gems)
    m = len(species)
    answer = [0, n-1]
    s = 0
    e = 0
    info = {}
    info[gems[s]] = 1
    
    while s < n and e < n:
        if len(info) == m:
            if answer[1] - answer[0] > e - s:
                answer[0], answer[1] = s, e
            if info[gems[s]] == 1:
                del info[gems[s]]
            else:
                info[gems[s]] -= 1
            s += 1
        else:
            e += 1
            if e == n:
                break
            if gems[e] in info.keys():
                info[gems[e]] += 1
            else:
                info[gems[e]] = 1
        
    answer[0] += 1
    answer[1] += 1
    
    return answer