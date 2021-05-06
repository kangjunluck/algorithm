n = int(input())
moneys = list(map(int,input().split()))
whole = int(input())

def check(mid):
    total = 0
    for money in moneys:
        if money >= mid:
            total += mid
        else:
            total += money
    if total <= whole:
        return True
    return False

l , r = 1, max(moneys)
while l <= r:
    mid = (l+r)//2
    if check(mid): l = mid + 1
    else: r = mid - 1
print(r)