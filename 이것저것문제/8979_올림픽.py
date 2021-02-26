import sys

input = sys.stdin.readline

n, target = map(int,input().split())

datas = []
want = 0
for i in range(n):
    country, gold, silver, blonze = map(int, input().split())
    if country == target:
        want = (gold, silver, blonze)
    else:
        datas.append((gold, silver, blonze))

cnt = 0
print(datas, want)
for data in datas:
    if data[0] > want[0]:
        cnt += 1
    elif data[0] == want[0]:
        if data[1] > want[1]:
            cnt += 1
        elif data[1] == want[1]:
            if data[2] > want[2]:
                cnt += 1
print(cnt+1)
                
