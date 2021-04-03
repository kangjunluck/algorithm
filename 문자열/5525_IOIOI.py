import sys

input = sys.stdin.readline


n = int(input()) # n+1개의 I, n개의 O
m = int(input()) # word의 길이

word = input()
ans = 0
for i in range(m-2*n):
    if word[i] == 'I':
        cnt = 0
        isTrue = True
        while cnt < 2*n:
            if word[i+1+cnt] == word[i+cnt]:
                isTrue = False
                break
            cnt += 1
        if isTrue:
            ans += 1

print(ans)