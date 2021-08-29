import sys

input = sys.stdin.readline

a = input().strip()
b = input().strip()

# aabbbaabaaa
# i         j
# bcnt = 0
# bcnt += 1
# 만나는 b의 갯수 홀수 i 움직이고 짝수이면 j가 움직인다
# 길이 같아지는데 b의 갯수가 홀수 뒤집고
# 구현


while len(b) != len(a):
    if b[-1] == 'A':
        b = b[:-1]
    else:
        b = b[:-1]
        b = b[::-1]


if a == b : print(1)
else: print(0)