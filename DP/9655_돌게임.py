import sys

input = sys.stdin.readline

# 짝수면 창영이 이기는데...?
n = int(input())

if n%2:
    print('SK')
else:
    print('CY')