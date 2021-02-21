import sys

input = sys.stdin.readline

word = input().strip()
cnts = [0 for _ in range(26)]

def isPali(word):
    global point
    i = 0
    while i < len(word):
        cnts[ord(word[i]) - ord('A')] += 1
        i += 1
    ispali = 0
    where = 100
    for j in range(26):
        if cnts[j]%2:
            ispali += 1
            where = j

    if ispali == 1:
        point = where
        return True
    elif ispali == 0:
        return True
    else:
        return False

point = 1000

result = []
if isPali(word):
    if point == 1000:
        #다 짝수개
        for k in range(25, -1, -1):
            if cnts[k] != 0:
                while cnts[k] > 0:
                    result.append(chr(ord('A') + k))
                    result = [chr(ord('A') + k)] + result
                    cnts[k] -= 2          
        print(''.join(result))      
    else:
        # 1개 홀수개
        result.append(chr(ord('A')+ point))
        cnts[point] -= 1
        for k in range(25, -1, -1):
            if cnts[k] != 0:
                while cnts[k] > 0:
                    result.append(chr(ord('A') + k))
                    result = [chr(ord('A') + k)] + result
                    cnts[k] -= 2    
        print(''.join(result))

else:
    print("I'm Sorry Hansoo")
