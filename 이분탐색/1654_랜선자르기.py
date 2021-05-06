n, m = map(int,input().split())
lans = [int(input()) for _ in range(n)]

def check(mid):
    cnt = 0
    for lan in lans:
        if lan >= mid:
            cnt += lan//mid
            if cnt >= m:
                return True
    return False

l , r = 1, max(lans)

while l <= r:
    mid = (l+r)//2
    if check(mid): l = mid+1
    else: r = mid -1

print(r)