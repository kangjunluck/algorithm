import sys

input = sys.stdin.readline

T = int(input())

for tc in range(1,T+1):
    n, m = map(int, input().split())
    data = [0] + list(map(int,input().split()))
    before = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        before[b].append(a)
    k = int(input())

    dp = [0] * (n+1)

    def findanswer(n):
        if dp[n]: return dp[n]
        maxi = 0
        for be in before[n]:
            maxi = max(maxi, findanswer(be))
        dp[n] = maxi + data[n]
        return dp[n]

    print(findanswer(k), "??")