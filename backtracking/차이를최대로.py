n = int(input())
data = list(map(int,input().split()))

#순열, 순서가 있는듯
check = [0]*n
sel = [10000]*n
answer = 0
def perm(idx, total, before):
    global answer
    if idx == n:
        answer = max(answer, total)
        return
    
    for i in range(n):
        if check[i]: continue
        check[i] = 1
        sel[idx] = data[i]
        if idx == 0: before = data[i]
        perm(idx+1, total+abs(data[i] - before), data[i])
        check[i] = 0
perm(0, 0, 0)
print(answer)