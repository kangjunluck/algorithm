# 중복 순열.... ㅠㅠ 구현을
import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int,input().split()))
calcs = list(map(int,input().split()))
cal = 1
new_list = []  # 1은 +, 2는 -, 3은 *, 4는 /
for calc in calcs:
    for i in range(calc):
        new_list.append(cal)
    cal += 1

m = len(new_list) # 연산자 갯수
result = []

for i in range(1<<m):
    cnt = 0
    ans = []
    for j in range(m):
        if i & (1<<j):
            cnt +=1
            ans.append(new_list[j])
    if cnt == n-1:
        if ans in result:
            pass
        else:
            result.append(ans)
real_result = []
