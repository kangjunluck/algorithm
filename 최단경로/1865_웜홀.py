import sys

input = sys.stdin.readline



def bellman(start):
    for o in range(n-1):
        for i in range(2*m+w):
            s,e,t = data[i]
            sumt = t + ans[s]
            if sumt < ans[e] and ans[s] != INF:
                ans[e] = sumt
    for i in range(2*m+w):
        s,e,t = data[i]
        sumt = t + ans[s]
        if sumt < ans[e] and ans[s] != INF:
            ans[e] = sumt
            return True
    return False

INF = sys.maxsize

T=int(input())

for tc in range(1,T+1):
    n, m, w = map(int,input().split())
    data = []
    for _ in range(m):
        ma, mb ,mc = map(int,input().split())
        data.append((ma, mb, mc))
        data.append((mb, ma, mc))
    whole = []
    for __ in range(w):
        wa, wb, wc = map(int, input().split())
        data.append((wa, wb, -wc))
        whole.append(wb)
    
    result = 'NO'
    for start in whole:
        ans = [INF for _ in range(n+1)]
        ans[start] = 0
        if bellman(start):
            result = 'YES'
            break
        
    print(result)