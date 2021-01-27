import sys

sys.stdin = open('7568_덩치.txt', 'r')
input = sys.stdin.readline
# n명이 비교를 할것이다.
n = int(input())
people=[]
for person in range(n):
    people.append(list(map(int,input().split())))

for info in people:
    cnt = 1
    for i in range(len(people)):
        if info[0] < people[i][0] and info[1] < people[i][1]:
            cnt += 1
    print(cnt, end=' ')