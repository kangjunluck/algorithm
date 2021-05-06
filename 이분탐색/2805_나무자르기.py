n, m = map(int,input().split())
trees = list(map(int,input().split()))

def check(mid):
    total = 0
    for i in range(n):
        tr = trees[i] - mid
        if tr > 0:
            total += tr
            if total >= m:
                return True
    return False

l, r = 1, max(trees)
while l < r:
    mid = (l+r)//2
    if check(mid): l = mid + 1
    else: r = mid
print(l - 1)