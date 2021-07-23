n, m = map(int, input().split())
data = list(map(str, input().split()))
data = sorted(data)
exp = ['a','e','i','o','u']
moim = 0
zaim = 0
for alpha in data:
    if alpha in exp:
        moim += 1
    else:
        zaim += 1


def combi(idx, start, use_mo, left_mo, use_ja, left_ja):
    if idx == n and use_mo > 0 and use_ja > 1:
        print(''.join(sel))
        return
    if use_mo + left_mo < 1 or use_ja + left_ja < 2:
        return
    for i in range(start, m):
        sel.append(data[i])
        if data[i] in exp:
            combi(idx+1, i+1, use_mo+1, left_mo-1, use_ja, left_ja)
        else:
            combi(idx+1, i+1, use_mo, left_mo, use_ja+1, left_ja-1)
        sel.pop()
sel = []
combi(0, 0, 0, moim, 0, zaim)