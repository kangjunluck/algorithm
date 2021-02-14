import sys

input = sys.stdin.readline

part_list = list(map(str, input().strip()))

result = ''
change = ''
for part in part_list:
    if part == ' ':
        if '<' in change:
            change += part
        else:
            result += change[-1::-1]
            result += ' '
            change = ''
    elif part == '<':
        if change:
            result += change[-1::-1]
            change = '<'
        else:
            change += part
    elif part == '>':
        change += part
        result += change
        change = ''

    else:
        change += part
result += change[-1::-1]
print(result)
