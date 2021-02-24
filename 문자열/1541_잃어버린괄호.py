import sys

input = sys.stdin.readline

words = input()
n = len(words)
calcu = 0
number = ''
s = []
numbers = []
isminus = False
for i in range(n):
    if words[i] == '+' or words[i] == '-':
        calcu += int(number)
        if isminus == True:
            number = '-'
        else:
            if words[i] == '+':
                number = ''
            else:
                isminus = True
                number = '-'
    else:
        number += words[i]
calcu += int(number)
print(calcu)
