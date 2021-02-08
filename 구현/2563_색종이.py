import sys

input = sys.stdin.readline

n = int(input())

all_list = []
for i in range(n):
    a, b = map(int, input().split())
    x_axis = list(range(a,a+10))
    y_axis = list(range(b,b+10))
    for x1 in x_axis:
        for y1 in y_axis:
            all_list.append((x1, y1))

set_list = set(all_list)
print(len(set_list))