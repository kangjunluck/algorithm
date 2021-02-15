import sys

input = sys.stdin.readline

part_list = list(map(str, input().strip()))

result = []
tag_list = []
change = []
for part in part_list:
    if part == '<':
        if change:
            result.append(''.join(change))
            change = []
        tag_list.append('<')
    elif part == '>':
        tag_list.append('>')
        result.append(''.join(tag_list))
        tag_list = []
    elif tag_list:
        tag_list.append(part)
    else:
        if part == ' ':
            result.append(''.join(change))
            result.append(' ')
            change = []
        else:
            change = [part] + change
result.append(''.join(change))

print(''.join(result).strip())