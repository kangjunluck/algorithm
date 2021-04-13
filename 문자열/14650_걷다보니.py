import sys

input = sys.stdin.readline

n = int(input())

sel = [-1 for _ in range(n)]
cnt = 0
def perm(idx):
    global cnt
    if idx == n:
        total = sum(sel)
        if total % 3 == 0:
            cnt += 1
        return
    for j in range(3):
        if idx == 0 and j == 0:
            continue
        sel[idx] = j
        perm(idx+1)
perm(0)
print(cnt)

