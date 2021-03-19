import sys

input = sys.stdin.readline

T =int(input())

for tc in range(1,T+1):
    n, m = map(int,input().split())
    
    node = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)
    visited = [0 for _ in range(n+1)]
    isTrue = True
    for i in range(1, n):
        if isTrue == False: break
        if visited[i]: continue
        q = [i]
        visited[i] = 1
        while q:
            if isTrue == False: break
            now = q.pop(0)
            for w in node[now]:
                if visited[w] == visited[now]:
                    isTrue = False
                    break
                if visited[w]:continue
                if visited[now] == 1:
                    visited[w] = 2
                    q.append(w)
                else:
                    visited[w] = 1
                    q.append(w)
    if isTrue:
        print('YES')
    else:
        print('NO')
