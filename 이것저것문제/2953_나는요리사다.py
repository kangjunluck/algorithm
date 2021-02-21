import sys

input = sys.stdin.readline

winner = 0
topscore = 0

for i in range(1,6):
    sum = 0
    for score in map(int, input().split()):
        sum += score
    if sum > topscore:
        topscore = sum
        winner = i
print(winner, topscore)