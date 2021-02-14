import sys

input = sys.stdin.readline

n, m = map(int, input().split())
cnt = int(input())
n_num = list(map(int,input().split()))
sum = 0

for i in n_num:
    sum += i*(n**(cnt-1))
    cnt -= 1

ans = []
while True:
    if sum // m:
        ans = [str(sum % m)] + ans
        sum //= m
    else:
        ans = [str(sum % m)] + ans
        break
print(' '.join(ans))

    
