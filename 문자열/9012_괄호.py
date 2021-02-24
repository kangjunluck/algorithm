import sys

input = sys.stdin.readline

T = int(input())

def isPerfect(words):
    s = []
    for word in words:
        if word == '(':
            s.append(word)
        else:
            if s:
                now = s.pop()
            else:
                return 'NO'
    if s:
        return 'NO'
    return 'YES'

for case in range(T):
    words = list(map(str, input().strip()))
    print(isPerfect(words))