import sys

input = sys.stdin.readline
tc = 1
while True:
    n = list(map(str,input().strip()))
    if n[0] == '-':
        break
    cnt = 0
    top = -1
    s = []
    for i in n:
        if i == '{':
            s.append(i)
            top += 1
        else:
            if s:
                s.pop()
                top -= 1
            else:
                s.append(i)
                top += 1
                cnt += 1
    if s:
        cnt += len(s)//2
    print('{}. {}'.format(tc, cnt))
    tc += 1
