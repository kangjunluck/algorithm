n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
check = [0] * n
sel = [0]*n
answer = 10000000
def perm(idx, total, before):
    global answer
    if idx == n:
        answer = min(answer, total)
        return
    if answer < total:
        return

    for i in range(n):
        if check[i]: continue

        if i != before and board[before][i] == 0:
            continue
        check[i] = 1
        sel[idx] = i
        if before == -1:
            perm(idx+1, total, i)
        else:
            perm(idx+1, total+board[before][i], i)
        check[i] = 0
check[0] = 1
perm(0, 0, 0)
print(answer)
