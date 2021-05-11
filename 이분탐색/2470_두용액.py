n = int(input())
data= list(map(int,input().split()))
data.sort()

str = abs(data[0] + data[-1])

ans = 0
l, r = 0, n-1
while l < r:
    num = data[l] + data[r]
    if abs(num) <= str:
        str = abs(num)
        ans = (data[l], data[r])
        if str == 0:
            break
    if num > 0:
        r -= 1
    else:
        l += 1

print(ans[0], ans[1])