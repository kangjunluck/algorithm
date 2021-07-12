import sys
sys.setrecursionlimit(1000000000)

def circulate(e):
    global Team
    visited[e] = 1
    check.append(e)
    if visited[pick[e]]:
        if pick[e] in check:
            Team.update(check[check.index(pick[e]):])
    else:
        circulate(pick[e])
    
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    visited = [0 for _ in range(n+1)]
    pick = [0] + list(map(int,input().split()))
    Team = set()
    for i in range(1,n+1):
        if visited[i]: continue
        check = []
        circulate(i)

    print(n - len(Team))



