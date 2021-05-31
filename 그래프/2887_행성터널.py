n = int(input())
data = []
for _ in range(n):
    x, y, z = map(int,input().split())
    data.append((x, y, x))

# 크루스칼 알고리즘, 최소신장트리
