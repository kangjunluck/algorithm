import heapq

def solution(n, s, a, b, fares):
    answer = 0
    # 3개의 지점 간의 최솟값을 구한다음에
    # 어느것이 짧은지 비교해야한다.
    
    # 최소 비용 구하기, 다익스트라 heapq 이용
    
    board = [[] for _ in range(n+1)]
    for x, y, z in fares:
        board[x].append((y,z))
        board[y].append((x,z))
    
    # start end 쌍 총 3개, s->c, c->a, c->b (c가 s나a나b와 같다면? 상관없네)
    def findshort(s):
        start = s
        q = []
        heapq.heappush(q, (start, 0))
        INF = 10000000
        ans = [INF for _ in range(n+1)]
        ans[start] = 0

        while q:
            now, short = heapq.heappop(q)
            for next, l in board[now]:
                suml = l + short
                if suml < ans[next]:
                    ans[next] = suml
                    heapq.heappush(q, (next, suml))
        return ans
    # s 에서 c까지를 구하기 위해
    together = findshort(s)
    print('-----------------')
    print(together)
    # c 에서 각 지점까지 최단거리
    mini = 10000000
    for c in range(1,n+1):
        #함께 탄 비용
        lonely = findshort(c)
        total = together[c] + lonely[a] + lonely[b]
        mini = min(total, mini)
    answer = mini
    
    return answer