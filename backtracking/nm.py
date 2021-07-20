n, m = map(int, input().split())

def answer(cnt, now):
    if cnt == m:
        print(*sel)
        return


    for i in range(now, n+1):
        sel.append(i)
        answer(cnt+1, i)
        sel.pop()

sel = []
answer(0, 1)
