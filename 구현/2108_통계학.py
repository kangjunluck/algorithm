import sys

input = sys.stdin.readline

n = int(input())

number = []
for case in range(n):
    number.append(int(input()))

# 산술평균
print(int(round(sum(number)/len(number),0)))
# 중앙값
number.sort()

print(number[len(number)//2])

# 최빈값
check_dict = {}
for num in number:
    check_dict[num] = check_dict.get(num, 0) + 1
reverse_dict = {}
for a, b in check_dict.items():
    if b in reverse_dict.keys():
        reverse_dict[b].append(a)
    else:
        reverse_dict[b] = [a]
sort_reverse_dict = sorted(reverse_dict.items(), reverse= True)
if len(sort_reverse_dict[0][1]) == 1:
    print(sort_reverse_dict[0][1][0])
else:
    print(sort_reverse_dict[0][1][1])


# 범위
range_far = max(number) - min(number)
print(range_far)