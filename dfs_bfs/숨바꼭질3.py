from collections import deque

n, k = map(int, input().split())
answer = -1
if n < k:
    visited = [-1] * 100000
    visited[n] = 1
    q = deque()
    q.append(n)
    visited[n] = 0
    while q:
        now = q.popleft()
        cnt = visited[now]
        if now == k:
            answer = cnt
            break
        nexta = now-1
        nextb = now+1

        nextc = 2*now
        while abs(now - k) > abs((nextc - k)):
            if visited[nextc] == -1:
                q.append(nextc)
                visited[nextc] = cnt
            else:
                if visited[nextc] > cnt:
                    visited[nextc] = cnt
                    q.append(nextc) # 왼쪽으로 넣어줘야하는데에
            nextc *= 2
            now *= 2

        if 0<=nexta<100000:
            if visited[nexta] == -1:
                visited[nexta] = cnt+1
                q.append(nexta)
            else:
                if visited[nexta] > cnt+1:
                    visited[nexta] = cnt+1
                    q.append(nexta)
                    
        if 0<=nextb<100000:
            if visited[nextb] == -1:
                visited[nextb] = cnt+1
                q.append(nextb)
            else:
                if visited[nextb] > cnt+1:
                    visited[nextb] = cnt+1
                    q.append(nextb)
        

    
else:
    answer = n-k
print(answer)



            

