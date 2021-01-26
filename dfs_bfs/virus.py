# que 함수 이용, --------------> 

# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7
import sys

sys.stdin=open("virus.txt","r")

n = int(sys.stdin.readline())  #컴퓨터 수
m = int(sys.stdin.readline())  #네트워크 연결 수

graph = [[] for _ in range(n+1)]
start=1


for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited= [0]*(n+1)
print(graph)
print(visited)
ans=0
que = [start]
while que:
    next=que.pop()
    if visited[next] : continue 
    visited[next]=True    # for문 안으로 넣자! ,deque로 해보기
    ans+=1
    for j in graph[next]:
        que = [j]+que



print(ans-1)