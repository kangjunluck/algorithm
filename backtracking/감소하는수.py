n = int(input())

def findans(idx, start):
    global answer
    global cnt
    global isEnd
    if isEnd:
        return
    if idx == l-1:
        cnt += 1
        if cnt == n+1:
            print(sel)
            answer = [str(i)] + sel[::-1]
            isEnd = True
        return
    for k in range(start, i):
        sel[idx] = str(num[k])
        findans(idx+1, k+1)

# 자리수 l
if n < 10:
    result = n
elif n > 1022:
    result = -1
else:
    l = 2
    cnt = 10
    isEnd = False
    answer = 0
    while True:
        for i in range(l-1,10):
            num = [j for j in range(i)]
            sel = [0]*(l-1)
            findans(0, 0)
            if isEnd:
                break
        if isEnd:
            break
        l += 1
    result = ''.join(answer)
print(result)

