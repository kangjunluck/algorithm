import sys

input = sys.stdin.readline

T = int(input())


for tc in range(1,T+1):
    n = int(input())
    dic = {}
    for _ in range(n):
        name, species = map(str,input().split())
        dic[species] = dic.get(species, 0) + 1
    ans = 1
    for m in dic.values():
        ans *= m+1
    print(ans-1)