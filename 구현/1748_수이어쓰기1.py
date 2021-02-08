import sys

input = sys.stdin.readline

n = int(input())

# sum = 0
# for i in range(1, n+1):
#     sum += len(str(i))
# print(sum)

k = len(str(n))
result = 0
while k > 0:
    result += k * (n - (10**(k-1)-1))
    n = 10**(k-1) - 1
    k -= 1

print(result)
    
