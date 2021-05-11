n, m = map(int,input().split())
A = list(map(int,input().split()))

def check(mid):
    cnt = 0
    for a in A:
        cnt += mid // a
        if cnt >= m:
            return True
    return False


l , r = 1, min(A)*m

while l <= r:
    mid = (l + r)//2
    if check(mid): r = mid - 1
    else: l = mid + 1

print(r + 1)