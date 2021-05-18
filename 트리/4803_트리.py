from collections import deque
tc = 1
while True:
    n, m = map(int,input().split())
    if n == 0 and m == 0:
        break
    data = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        data[a].append(b)
        data[b].append(a)
    visited = [0 for _ in range(n+1)]
    cnt = 0
    for i in range(1, n+1):
        if visited[i]: continue

        isTrue = True
        q = deque()
        q.append(i)
        # 이문제는 방문 체크를 나중에 해야한다.
        while q:
            now = q.popleft()
            if visited[now] == 1:
                isTrue = False
            visited[now] = 1
            for j in data[now]:
                if visited[j] == 0:
                    q.append(j)
        if isTrue:
            cnt += 1
    if cnt == 0:
        print('Case {}: No trees.'.format(tc))
    elif cnt == 1:
        print('Case {}: There is one tree.'.format(tc))
    else:
        print('Case {}: A forest of {} trees.'.format(tc, cnt))

    tc += 1