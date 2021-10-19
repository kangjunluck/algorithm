T = int(input())

for tc in range(1,T+1):
    n = int(input())
    data = list(map(int,input().split()))
    answer = 0
    # 4개의 역을 뽑아야한다.
    def combi(idx, start):
        global answer
        if idx == 4:
            if sel[-1] - sel[0] != n-1:
                a = data[sel[0]]
                b = data[sel[1]]
                c = data[sel[2]]
                d = data[sel[3]]
                answer = max(answer, (a + b)**2 + (c+d)**2, (b+c)**2 + (a+d)**2)

            return

        if idx == 0:
            for i in range(start, n):
                sel.append(i)
                combi(idx+1, i+1)
                sel.pop()
        else:
            for i in range(start+1, n):
                sel.append(i)
                combi(idx+1, i+1)
                sel.pop()

    sel = []
    combi(0, 0)
    print('#{} {}'.format(tc, answer))