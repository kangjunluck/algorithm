import sys

sys.stdin=open("data.txt","r")

def dfs(i) :
    if visited[i] : return
    visited[i]=True
    ans.append(i)
    for j in graph[i] :
        dfs(j)

# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]


for _ in range(m) :
    a,b = map(int,  sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [0]*(n+1)   # 도착한적 있는지 없는지 확인을 위한

print(visited)

for a in graph :
    a.sort()
ans=[]
print(graph)


dfs(v)
print(ans)

ans=[]
visited = [False for _ in range(n+1)]

que = [v]
while que :
    next = que.pop()
    if visited[next] : continue
    visited[next]=True
    ans.append(next)
    for i in graph[next] :
        que = [i]+que

print(ans)

# print(' '.join(map(str,ans)))