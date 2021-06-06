import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

uf = [i for i in range(n)]

def find(a):
    if uf[a] == a: return a
    uf[a] = find(uf[a])
    return uf[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b: uf[a] = b
    else: uf[b] = a


data = []
isDone = True
for i in range(m):
    x, y = map(int,input().split())
    data.append((x, y))

result = 1
for step in data:
    a, b = step
    if find(a) == find(b):
        print(result)
        isDone = False
        break
    else:
        union(a, b)
        result += 1
if isDone:
    print(0)

