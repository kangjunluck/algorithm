import sys

input = sys.stdin.readline

word = input()

n = len(word)

ans = []

# 선택 갯수
for i in range(1, n+1):
    for j in range(n-i):
        part = word[j:j+i]
        ans.append(part)
print(len(set(ans)))

        