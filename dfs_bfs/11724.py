import sys

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
visited[0]=1
#dfs로 풀어보자.
def dfs(i):  # i시작점
    if visited[i]:return
    else:
        visited[i]=1
        for k in board[i]:
            dfs(k)
ans=0
for i in range(1,n+1):
    if visited[i]==0:
        dfs(i)
        ans+=1
print(ans)