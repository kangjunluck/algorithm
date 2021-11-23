import heapq

n, m = map(int, input().split())
data = [[] for _ in range(n+1)]
degree = [0] *(n+1)
q = []
answer = []
for _ in range(m):
    a, b = map(int,input().split())
    data[a].append(b)
    degree[b] += 1

for i in range(1,n+1):
    if degree[i] == 0:
        heapq.heappush(q, i)

while q:
    now = heapq.heappop(q)
    answer.append(now)
    for j in data[now]:
        degree[j] -= 1
        if degree[j] == 0:
            heapq.heappush(q, j)

print(*answer)
