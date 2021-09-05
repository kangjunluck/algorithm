import sys
input = sys.stdin.readline

n, m, k = map(int,input().split())
guns = list(map(int, input().split()))
guns.sort()
anis = []
for _ in range(m):
    a, b = map(int,input().split())
    anis.append((a, b))
cnt = 0
for ani in anis:
    l = 0
    r = n-1
    mid = (l+r)//2
    while l < r:
        mid = (l+r)//2
        if guns[mid] < ani[0]: l = mid + 1
        else: r = mid
    if abs(guns[mid] - ani[0]) + ani[1] <= k:
        cnt += 1
    elif (abs(guns[mid+1] - ani[0]) + ani[1]) <= k:
        cnt += 1

print(cnt)