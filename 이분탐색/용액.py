n = int(input())
data = list(map(int,input().split()))

l = 0
r = n-1
answer = 2000000000
ansl = l
ansr = r
while l<r:
    sumdata = data[l] + data[r]
    if abs(sumdata)<answer:
        answer = abs(sumdata)
        ansl = l
        ansr = r

    if sumdata > 0:
        r -= 1
    else:
        l += 1

print(data[ansl], data[ansr])