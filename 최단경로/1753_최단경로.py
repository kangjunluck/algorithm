import sys
from queue import PriorityQueue

input = sys.stdin.readline

n, m = map(int, input().split())

start = int(input())
inf = 100000000
board = [[inf for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int,input().split())
    if board[a][b] > c:
      board[a][b] = c
for i in range(n+1):
    board[i][i] = 0

visited = [0 for _ in range(n+1)]
visited[0] = 1


# 가장 최소 거리를 가지는 정점 찾기
def findidx(ans):
    mini = inf
    idx = 0
    for k in range(1, n+1):
        if ans[k] < mini and visited[k] == 0:
            mini = ans[k]
            idx = k
    return idx

# 다익스트라를 수행하는 함수
def dijkstra(start):
    ans = board[start]
    visited[start] = 1
    for i in range(n-1):
        now = findidx(ans)
        visited[now] == 1
        for j in range(n+1):
            if visited[j] == 0:
                if (ans[now] + board[now][j]) < ans[j]:
                    ans[j] = (ans[now] + board[now][j])
    return ans
result = dijkstra(start)
for mm in range(1, n+1):
    if result[mm] == inf:
        print('INF')
    else:
        print(result[mm])