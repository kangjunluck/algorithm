import sys

input = sys.stdin.readline

a = input().strip()
b = input().strip()



while len(b) != len(a):
    if b[-1] == 'A':
        b = b[:-1]
    else:
        b = b[:-1]
        b = b[::-1]


if a == b : print(1)
else: print(0)