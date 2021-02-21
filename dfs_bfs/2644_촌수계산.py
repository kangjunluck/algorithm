import sys

input = sys.stdin.readline

n = int(input())

a, b = map(int,input().split())

m = int(input())

relation = [[] for _ in range(n+1)]

for _ in range(m):
    par, son = map(int,input().split())
    relation[par].append(son)
# 최상위 부모를 구하고 dfs를 해야한다. 최소공통조상? (LCA) 배우기..
def dfs(k):
    sum = 1
    for s in relation[k]:
        sum += dfs(s)
    if k == a or k == b:
        return sum

for i in range(1,n+1):
    dfs(i)
