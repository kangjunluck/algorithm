T = int(input())

def find(a):
    if uf[a]==a: return a
    uf[a] = find(uf[a])
    return uf[a]

def union(a, b):
    a = find(a)
    b = find(b)

    # 이런 풀이 굿..
    if a != b:
        uf[a] = b
        number[b] += number[a]

for tc in range(1,T+1):
    uf = dict()
    number = dict()
    f = int(input())

    for _ in range(f):
        a, b = map(str, input().split())

        # 이런 풀이 굿..
        if a not in uf:
            uf[a] = a
            number[a] = 1
        if b not in uf:
            uf[b] = b
            number[b] = 1
            
        union(a, b)
        print(number[find(a)])




    
