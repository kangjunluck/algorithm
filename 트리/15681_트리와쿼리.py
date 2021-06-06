import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, r, q = map(int,input().split())

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
    
# 0으로 해줘야 방문 표시도 해줄 수 있다.
number = [0 for _ in range(n+1)]
# 서브트리의 수를 저장해줘야한다

def findcnt(r):
    number[r] = 1
    for i in tree[r]:
        if not number[i]:
            findcnt(i)
            number[r] += number[i]
        
findcnt(r)
for __ in range(q):
    u = int(input())
    print(number[u])