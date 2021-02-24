import sys

input = sys.stdin.readline

n = int(input())
dict = {}
for i in range(n):
    word = input().strip()
    m = len(word)
    if word in dict:
        continue
    dict[word] = dict.get(word, m)
res = sorted(dict.items(), key = lambda x:(x[1],x[0]))
for re in res:
    print(re[0])