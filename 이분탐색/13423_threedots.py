T = int(input())

for tc in range(1,T+1):
    n = int(input())
    data = list(map(int,input().split()))
    data.sort()
    cnt = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if data[k] - data[j] == data[j] - data[i]:
                    cnt += 1
    print(cnt)