#stack으로 풀어야 한단다...
import sys

input = sys.stdin.readline

word = input()

def isperfect(word):
    word_list = []
    for i in word:
        if len(word_list) == 0 and (i == ']' or i == ')'):
            return False

        elif i == '(' or i == '[':
            word_list.append(i)

        elif i == ')' and word_list[-1] == '(':
            word_list.pop()
        elif i == ']' and word_list[-1] == '[':
            word_list.pop()
    if len(word_list) > 0:
        return False
    return True

def calculate(word):
    sum_list = []
    for i in word:
        if i == '(' or i == '[':
            sum_list.append(i)
        elif i == ')' and sum_list[-1] == '(':
            sum_list.pop()
            sum_list.append(2)
        elif i == ')' and sum_list[-1] > 0:
            part_sum = 0
            for j in range(len(sum_list)-1, -1, -1):
                if type(sum_list[j]) == int:
                    part_sum += sum_list[j]
                    sum_list.pop()
                elif sum_list[j] == '(':
                    sum_list.pop()
                    break
            sum_list.append(part_sum * 2)
        
        elif i == ']' and sum_list[-1] == '[':
            sum_list.pop()
            sum_list.append(3)
        
        elif i == ']' and sum_list[-1] > 0:
            part_sum = 0
            for j in range(len(sum_list)-1, -1, -1):
                if type(sum_list[j]) == int:
                    part_sum += sum_list[j]
                    sum_list.pop()
                elif sum_list[j] == '[':
                    sum_list.pop()
                    break
            sum_list.append(part_sum * 3)
    return sum_list

if isperfect(word):
    print(sum(calculate(word)))
else:
    print(0)