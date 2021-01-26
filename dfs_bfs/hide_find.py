#bfs일것 같아. 최소 시간 구하기 문제
import sys
from collections import deque

sys.stdin=open('hide_find.txt',"r")

n,m = map(int, sys.stdin.readline().split())

#동생은 가만히 있고 수빈이만 움직인다.

#(수빈이의 위치, 움직인 횟수(및 시간))   왔던곳 가는 경우는 제외하자. 최소거리니까
# ans=0
# if n>=m: print(m-n)
# else:
#     while 2*n<m:
#         n=2*n
#         ans+=1
    
#     if m-n>=2*n-m+1:
#         ans=ans+2*n-m+1
#         print(ans)
#     else:
#         ans=ans+m-n
#         print(ans)
q = deque()
q.append((n,0))

while q:
    now=q.popleft()
    
    if now[0]==m:
        break

    a=[now[0]-1,now[0]+1,now[0]*2]
    b=now[1]+1

    for i in a:
        if i==m:
            break  
        else:
            q.append((i,b))
    
    if a[0] == m or a[1] == m or a[2] == m:
        break
print(b)