import sys

input = sys.stdin.readline

word = list(map(str,input().strip()))

result = 0
check = ''
while word:
    now = word.pop()
    if check:
        if now == '=' or now == '-' or now == 'j':
            result += 1
            check = now
        else:
            if check == 'j':
                if now == 'n' or now == 'l':
                    result += 1
                    check = ''
                else:
                    result += 2
                    check = ''
            elif check == '=z':
                if now == 'd':
                    result += 1
                    check = ''
                else:
                    result += 2
                    check = ''
            else:
                if now == 'z':
                    check += now
                else:
                    result += 1
                    check = ''
    else:
        if now == '=' or now == '-' or now == 'j':
            check += now
        else:
            result += 1
if check:
    result += 1
print(result)