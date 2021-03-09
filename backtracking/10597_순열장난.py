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
    if (idx <= length-1) and int(data[idx])>0 :
        a = data[idx]
        if int(a) <= N and check[int(a)-1] == 0: 
            check[int(a)-1] = 1    
            word.append(a)
            find(idx+1, word)
            word.pop()
            check[int(a)-1] = 0
    if idx+1 <= length-1:
        a = data[idx:idx+2]
        if int(a) <= N and check[int(a)-1] ==0 :
            check[int(a)-1] = 1
            word.append(a)
            find(idx+2, word)
            word.pop()
            check[int(a)-1] = 0
    return
find(0)
print(result[0])