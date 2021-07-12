from collections import deque

T = int(input())

for tc in range(1,T+1):
    a, b = map(int, input().split())
    q = deque()
    q.append((a, ''))
    visited = [0 for _ in range(10000)]
    answer = 0

    while q:
        now, step = q.popleft()
        if now == b:
            answer = step
            break
        visited[now] = 1
        first = (now*2) % 10000
        if visited[first] == 0:
            q.append((first, step+'D'))

        second = 9999 if now == 0 else now-1
        if visited[second] == 0:
            q.append((second, step+'S'))

        l = now//1000
        third = (now*10)%10000 + l
        if visited[third] == 0:
            q.append((third, step+'L'))

        m = (now%10) * 1000
        fourth = (now//10) + m
        if visited[fourth] == 0:
            q.append((fourth, step+'R'))
    print(answer)





