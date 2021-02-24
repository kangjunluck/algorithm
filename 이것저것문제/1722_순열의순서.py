import sys

input = sys.stdin.readline

n = int(input())

data = list(map(int,input().split()))

arr = [ i for i in range(1, n+1)]
sel = [0] * n
cnt = 0
check = 0
def perm(idx, target, check):
    global cnt
    if idx == n:
        cnt += 1
        if cnt == target:
            print(*sel)
            return
    else:
        for j in range(n):
            if check & (1<<j) : continue
            sel[idx] = arr[j]
            perm(idx + 1, target, check | (1<<j))


def order(idx, array, check):
    global cnt
    if idx == n:
        cnt += 1
        if sel == array:
            print(cnt)
            return
    else:
        for j in range(n):
            if check & (1<<j) : continue
            sel[idx] = arr[j]
            order(idx + 1, array, check | (1<<j))

if data[0] == 1:
    perm(0, data[1], check)
else:
    data.pop(0)
    order(0, data, check)