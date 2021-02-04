import sys
from collections import deque

sys.stdin=open('14891_톱니바퀴.txt','r')
input = sys.stdin.readline

box = [[]]
for _ in range(4):
    box.append(list(map(int, input().strip())))

n = int(input())

def right_sum(wheel):
    a = wheel.pop()
    change_wheel = [a] + wheel
    return change_wheel
def left_sum(wheel):
    a = wheel.pop(0)
    change_wheel = wheel + [a]
    return change_wheel

for step in range(n):
    start_wheel, start_way = map(int, input().split())
    visited = [0 for __ in range(5)]
    visited[start_wheel] = visited[0] = 1
    q = deque()
    q.append((start_wheel, start_way))
    while q:
        now_wheel, way = q.popleft()
        r_wheel = now_wheel + 1
        l_wheel = now_wheel - 1
        if way == -1:
            if 0<r_wheel<5 and visited[r_wheel] == 0:
                if box[now_wheel][2] != box[r_wheel][6]:
                    visited[r_wheel] = 1
                    q.append((r_wheel, 1))      
            if 0<l_wheel<5 and visited[l_wheel] == 0:
                if box[now_wheel][6] != box[l_wheel][2]:
                    visited[l_wheel] = 1
                    q.append((l_wheel, 1))
            box[now_wheel] = left_sum(box[now_wheel])
        if way == 1:
            if 0<r_wheel<5 and visited[r_wheel] == 0:
                if box[now_wheel][2] != box[r_wheel][6]:
                    visited[r_wheel] = 1
                    q.append((r_wheel, -1))      
            if 0<l_wheel<5 and visited[l_wheel] == 0:
                if box[now_wheel][6] != box[l_wheel][2]:
                    visited[l_wheel] = 1
                    q.append((l_wheel, -1))
            box[now_wheel] = right_sum(box[now_wheel])
sum = 0
for i in range(1, 5):
    sum += box[i][0]*(2**(i-1))
print(sum)