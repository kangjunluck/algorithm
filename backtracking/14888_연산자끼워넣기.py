import sys

input = sys.stdin.readline

def perm(idx):
    global mini, maxi
    if idx == n-1:
        #다채워졋다.
        ans = numbers[0]
        num = 1
        for k in sel:
            if k == 0:
                ans += numbers[num]
            elif k == 1:
                ans -= numbers[num]
            elif k == 2:
                ans *= numbers[num]
            else:
                ans = int(ans/numbers[num])
            num += 1
        mini = min(mini, ans)
        maxi = max(maxi, ans)
        return
    for w in range(4): # 4개의 선택지를 인덱스로 하여 본다.
        if calc[w]:
            calc[w] -= 1
            sel[idx] = w
            perm(idx+1)
            calc[w] += 1

n = int(input())

numbers = list(map(int,input().split()))
calc = list(map(int,input().split())) # 연산자 갯수,
sel = [0 for _ in range(n-1)]
mini = 1000000000
maxi = -1000000000

perm(0)

print(maxi)
print(mini)