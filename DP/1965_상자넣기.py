#증가하는 수열이랑 같다....
import sys

input = sys.stdin.readline

n = int(input())

data = list(map(int,input().split()))

dp = [0 for _ in range(n)]
dp[-1] = 1
def findand():
    for i in range(n-1, -1, -1):

        if i == n-1:
            dp[i] == 0
            continue
        
        maxi = 0
        for j in range(i+1, n):
            if data[j] > data[i] and maxi <= dp[j]:
                maxi = dp[j]
        if maxi:
            dp[i] = maxi + 1
        else:
            dp[i] = 1

    return max(dp)

print(findand())



