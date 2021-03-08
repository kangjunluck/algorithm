import sys

input = sys.stdin.readline

data = input().strip()
length = len(data) # 길이를 통해 N의 값을 구해야한다.
k = length
n = 1
while k // ( 10**n - 10**(n-1) ):
    k -= ( 10**n - 10**(n-1) )
    n += 1
N = 10**(n-1) + (k)//n - 1

check = [0 for _ in range(N)]
result = []
def find(idx, word=[]):
    global result
    if len(word) > N:
        return
    if len(word) == N:
        result.append(' '.join(word))
        return
    for i in range(idx, idx+2):
        if (i == idx) and (i <= length-1):
            a = data[i]
            if int(a) > N or check[int(a)-1]: continue
            check[int(a)-1] = 1    
            word.append(a)
            find(i+1, word)
            word.pop()
            check[int(a)-1] = 0
        elif (i == idx+1) and (i <= length-1):
            a = data[i-1:i+1]
            if int(a) > N or check[int(a)-1] : continue
            check[int(a)-1] = 1
            word.append(a)
            find(i+1, word)
            word.pop()
            check[int(a)-1] = 0
    return
find(0)
print(result[0])