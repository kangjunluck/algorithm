# 홀수 합성수 문제
# 조합으로 푸는데 dp로는 못푸나?

import sys
sys.setrecursionlimit(10000000)
answer = 0
isFind = False
def solution(n):
    global answer
    if n%2:
        l = n//2 + 1
    else:
        l = n//2
    odd = [2*k + 1 for k in range(l)]
    
    #조합을 만들면 된다.

    def makeAns(idx, start, total):
        global isFind
        global answer
        if isFind:
            return
        if total > n:
            return
        if total == n:
            answer = idx
            isFind = True
            return
        for i in range(start, l):
            total += odd[i]
            makeAns(idx+1, i+1, total)
            total -= odd[i]

    makeAns(0, 0, 0)
    
    return answer

print(solution(13))