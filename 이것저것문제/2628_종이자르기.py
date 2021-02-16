import sys

input = sys.stdin.readline

n, m = map(int, input().split())
methodr = [0, m]
methodc = [0, n]
num = int(input())

for step in range(num):
    way, where = map(int,input().split())
    if way == 0:
        if where == 0 or where == m:
            pass
        else:
            methodr.append(where)
    else:
        if where == 0 or where == n:
            pass
        else:
            methodc.append(where)
methodr.sort()
methodc.sort()
max = 0
for i in range(1, len(methodr)):
    for j in range(1, len(methodc)):
        a = methodr[i] - methodr[i-1]
        b = methodc[j] - methodc[j-1]
        multi = a * b
        if max < multi:
            max = multi
print(max)