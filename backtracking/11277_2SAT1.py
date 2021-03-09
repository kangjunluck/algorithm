import sys

input = sys.stdin.readline

n, m = map(int, input().split())

sel = [0 for _ in range(n)]

data = []
for _ in range(m):
    a, b = map(int ,input().split())
    data.append((a, b))
isResult = 0
def cases(idx):
    global isResult
    if idx == n:
        isAnswer = True
        for step in data:
            x, y = step[0], step[1]
            if x < 0: 
                if sel[x*(-1) - 1] == 0: partA = 1
                else: partA = 0
            else: partA = sel[x - 1]
            if y < 0:
                if sel[y*(-1) - 1] == 0: partB = 1
                else: partB = 0
            else: partB = sel[y - 1]
            if (partA | partB) != 1:
                isAnswer = False
                break
        if isAnswer:
            isResult = 1
        return

    for i in range(2):  # 0 false, 1 True
        sel[idx] = i
        cases(idx+1)

cases(0)
print(isResult)