import sys

input = sys.stdin.readline

n = int(input())

num_list = []
for i in range(n):
    m = int(input())
    if m != 0:
        num_list.append(m)
    else:
        if len(num_list)==0:
            print(0)
            continue
        else:
            abs_list = []
            for number in num_list:
                if number > 0:
                    abs_list.append(number)
                else:
                    abs_list.append(-number)
            min_number = min(abs_list)

            result = []
            for j in range(len(abs_list)):
                if abs_list[j] == min_number:
                    result.append(num_list[j])
            ans = min(result)
            num_list.remove(ans)
            print(ans)