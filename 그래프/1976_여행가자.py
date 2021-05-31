n = int(input())
m = int(input())

uf = [p for p in range(n+1)]

def find(a):
    if uf[a] == a: return a
    uf[a] = find(uf[a])
    return uf[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b: uf[a] = b
    else:
        uf[b] = a

for i in range(1, n+1):
    data = list(map(int,input().split()))
    for j in range(n):
        if data[j] == 1:
            union(i, j+1)

route = list(map(int, input().split()))

ans = 'YES'
for l in range(len(route) - 1):
    if find(route[l]) != find(route[l+1]):
        ans = 'NO'
        break
print(ans)

