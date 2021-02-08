import sys
import heapq


sys.stdin = open('fight.txt','r')
input = sys.stdin.readline

n = int(input())

num_list = []
for i in range(n):
    m = int(input())
    if m != 0:
        heapq.heappush(num_list, (abs(m), m))
    elif m == 0 and len(num_list) == 0:
        print(0)
    else:
        print(heapq.heappop(num_list)[1])
