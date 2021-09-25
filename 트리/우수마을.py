import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)

n = int(input())
# dp 문제이다.....
numbers = list(map(int, input().split()))
numbers = [0] + numbers
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

# 깊이를 내려갈때마다, 최댓값 찾기, 전이 우수가 아니면, 다음은 우수일수도 아닐수도 있따.
check = [0]*(n+1)
dp = [[0]*2 for _ in range(n+1)]
def dfs(i):
    check[i] = 1
    dp[i][0] = numbers[i]
    for nx in tree[i]:
        if not check[nx]:
            dfs(nx)
            dp[i][0] += dp[nx][1]
            dp[i][1] += max(dp[nx][0], dp[nx][1])
dfs(1)
print(max(dp[1][0], dp[1][1]))



