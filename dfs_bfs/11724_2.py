import sys

from collections import deque

sys.stdin=open('11724.txt',"r")
input = sys.stdin.readline
# n = 정점의 개수, m = 간선의 개서
n, m = map(int, input().split())
# 각 원소의 연결된 정점 리스트 표시
board=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int, input().split())
    board[a].append(b)
    board[b].append(a)

visited=[0]*(n+1)

q=deque()
ans=0
for i in range(1,n+1):
    if visited[i]==1 : continue
    ans+=1
    q.append(i)
    while q:
        now=q.popleft()
        if visited[now] : continue
        else:
            visited[now]=True
            for i in board[now]:
                q.append(i)

print(ans)