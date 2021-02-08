import sys

input = sys.stdin.readline

bracket = input()

ans = 0
save_list = []
while True:
    if '(]' in bracket or '[)' in bracket or '[' == bracket[-1] or ']' == bracket[0] or '(' == bracket[-1] or ')' == bracket[0]:
        ans = 1
        break
    elif '()' in bracket:
        bracket = bracket.replace('()','2')
        save_list.append(2)
    elif '[]' in bracket:
        bracket = bracket.replace('[]','3')
        save_list.append(3)
    else:
        break

if ans == 1:
    print(0)
else:
    list_bracket = list(bracket.strip())
    for i in range(len(list_bracket)):
        if list_bracket[i] == '3':
            list_bracket.remove('3')
            list_bracket.insert(i, 3)
        elif list_bracket[i] == '2':
            list_bracket.remove('2')
            list_bracket.insert(i, 2)
    while save_list:
        now = save_list.pop()
        now_index = list_bracket.index(now)
        left_index = now_index - 1
        right_index = now_index + 1
        if list_bracket[left_index] == '(' and list_bracket[right_index] == ')':
            multi_str = now*2
            list_bracket.remove(now)
            trash = list_bracket.pop(left_index)
            trash2 = list_bracket.pop(left_index)
            list_branket.insert(left_index, multi_str)
            save_list.append(multi_str)


        elif list_bracket[left_index] == '[' and list_bracket[right_index] == ']':
            multi_str = now*3
            list_bracket.remove(now)
            trash = list_bracket.pop(left_index)
            trash2 = list_bracket.pop(left_index)
            list_branket.insert(left_index, multi_str)
            save_list.append(multi_str)

        elif type(list_bracket[left_index]) == int:
            multi_str = now*list_bracket[left_index]
            list_bracket.remove(now)
            trash = list_bracket.pop(left_index)
            list_branket.insert(left_index, multi_str)
            save_list.append(multi_str)
        elif 

            