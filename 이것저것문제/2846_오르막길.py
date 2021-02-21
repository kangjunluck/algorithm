import sys

input = sys.stdin.readline

n = int(input())

steps = list(map(int, input().split()))

start = steps[0]
maxi = 0
part_sum = 0
for step in steps:
    if step > start:
        part_sum += step - start  
    else:
        if part_sum > maxi:
            maxi = part_sum
        part_sum = 0
    start = step
if part_sum != 0:
    if part_sum > maxi:
        maxi = part_sum
print(maxi)