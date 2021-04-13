import sys

input = sys.stdin.readline

n = int(input())

def  isPali(num):
    nums = str(num)
    if nums == nums[::-1]:
        return True
    return False

#에라토스테네스의 체를 만들기
m = 1003001
a = [True for _ in range(m+1)]
a[1] = False
a[0] = False
for i in range(2, m):
    if a[i]:
        for j in range(i*2, m, i):
            a[j] = False
ans = 1003001
while n <= 1003001:
    if  a[n] and isPali(n):
        ans = n
        break
    n += 1
print(ans)


