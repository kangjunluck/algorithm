t = int(input())
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

# 정렬을 할 수 가 없다.
# 부분 집합의 합을 모두 확인한 뒤에 더해야하지 않을까.

# a의 갯수부터 1~n개
answer = 0
cnta = 0
while cnta < n:
    for i in range(0, n-cnta):
        suma = sum(a[i:i+cnta])
        
        cntb = 0
        while cntb < m:
            for j in range(0, m-cntb):
                sumb = sum(b[i:i+cntb])
                if suma + sumb == t:
                    answer += 1
            cntb += 1
    cnta += 1 

print(answer)