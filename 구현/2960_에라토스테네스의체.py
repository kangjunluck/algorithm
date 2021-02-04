import sys

input = sys.stdin.readline

n, k = map(int, input().split())

num_list = list(range(2,n+1))

cnt = 0
standard = 0
while standard < 1:
    now = num_list[0]
    multi_num = num_list[-1]//now
    for i in range(1, multi_num+1):
        if now*i in num_list:
            num_list.remove(now*i)
            cnt += 1
            if cnt == k:
                print(now*i)
                standard = 1
                break