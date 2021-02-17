# 이거 그거 아닌가 버블정렬?
import sys

input = sys.stdin.readline

array = list(map(int, input().split()))
n = len(array)

for i in range(n, 0, -1):
    for j in range(1, i):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            print(*array)