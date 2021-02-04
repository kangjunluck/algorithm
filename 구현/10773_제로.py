import sys

# sys.stdin = open('10773_제로.txt', 'r')
input = sys.stdin.readline

n = int(input())

number = []

for case in range(n):
    num = int(input())
    if num == 0:
        number.pop()
    else:
        number.append(num)

print(sum(number))