import sys
sys.setrecursionlimit(1000000)

n, m = map(int,input().split())

# 부모 노드를 넣어 두는 유니온 파인드 집합을 만든다. 초기는 자기 자신을 부모 노드로
uf = [ i for i in range(n+1) ]

# 자신의 최상위 부모노드를 찾는다.
def find(a):
    if uf[a]==a: return a
    uf[a] = find(uf[a])
    return uf[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b: uf[a] = b
    else: uf[b] = a


for _ in range(m):
    k, x, y = map(int, input().split())
    if k == 1:
        if find(x) == find(y):
            print('YES')
        else:
            print('NO')
    else:
        union(x, y)
