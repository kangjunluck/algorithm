import sys

input = sys.stdin.readline

case = int(input())

for i in range(case):
    ac_info = list(map(str,input().strip()))
    n = int(input())
    array_word = input()
    if ac_info.count('D') > n:
        print('error')

    # real_list = list(map(int, a.strip('[').strip(']').split(','))) 이거 왜 안되는거지 진짜...


    else:
        array_list = list(map(str, array_word[1:-2].split(',')))
        change = 0
        for step in ac_info:
            if step == 'R':
                change += 1
            else:
                if change % 2:
                    trash = array_list.pop()
                else:
                    trash = array_list.pop(0)
        if change % 2:
            array_list.reverse()
        print('[', end='')
        print(','.join(array_list), end='')
        print(']')