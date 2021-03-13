import sys

input = sys.stdin.readline

n = int(input())

def perm(idx):
    global cnt
    global isFind
    if isFind:
        return
    if idx == len(sel):
        cnt += 1
        if cnt == n:
            ans.append(sel)
            isFind = True
        return
    for j in range(10):
        if isFind: break
        if idx >= 1:
            if j >= sel[idx-1]: continue
            sel[idx] = j
            perm(idx+1)
        else:
            if j == 0: continue
            sel[idx] = j
            perm(idx+1)


if n <= 10:
    print(n-1)
elif n > 1023:
    print(-1)
else:
    cnt = 10
    i = 2
    isFind = False
    ans = []
    while True:
        if isFind: break
        sel = [0 for _ in range(i)]
        perm(0)
        i += 1
    for num in ans[0]:
        print(num, end='')