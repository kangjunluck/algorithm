import sys

sys.stdin = open('fight.txt','r')
input = sys.stdin.readline

n = int(input())

num_list = []
for i in range(n):
    m = int(input())
    if m > 0:
        num_list.append((m, m))
    elif m < 0:
        num_list.append((-m, m))
    else:
        if len(num_list)==0:
            print(0)
            continue
        else:
            num_list = sorted(num_list, key=lambda x:(-x[0], -x[1]))
            now = num_list.pop()
            print(now[1])