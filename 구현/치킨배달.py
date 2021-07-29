n, m = map(int, input().split())
map = [list(map(int,input().split())) for _ in range(n)]

homes = []
chickens = []
num = 0
for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            homes.append((i, j))
        elif map[i][j] == 2:
            chickens.append((i, j))
            num += 1

def combi(idx, start):
    global answer
    if idx == m:
        isEnd = True
        chic_length = 0
        for a, b in homes:
            if answer < chic_length:
                isEnd = False
                break
            mini = 10000
            for c, d in sels:
                mini = min(mini, abs(a-c)+abs(b-d))
            chic_length += mini
        if isEnd:
            if answer > chic_length:
                answer = chic_length
        return

    for k in range(start, num):
        sels[idx] = chickens[k]
        combi(idx+1, k+1)

answer = 100000
sels = [0]*m
combi(0, 0)
print(answer)
        