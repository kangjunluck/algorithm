import sys

sys.stdin = open('1316_그룹단어체커.txt', 'r')
input = sys.stdin.readline

# 첫 출 cases는 100보다 작거나 같은 자연수.
n = int(input())

ans=0
for case in range(n):
    word = input().strip()
    check_alpha = ''
    for alpha in word:
        # 체크알파 안에 알파벳이 있는가.
        if alpha not in check_alpha:
            #없으면 그냥 넣어준다.
            check_alpha += alpha
        # 있으면 두가지로 나뉜다. 바로 전에랑 같은가 다른가.
        else:
            # 같으면 그대로 넣어준다.
            if alpha == check_alpha[-1]:
                check_alpha += alpha
            # 다르면 그 즉시 반복문을 종료한다.
            else:
                break
    # 체크알파와 처음 단어가 같으면 그 단어는 추가해주고
    if len(check_alpha) == len(word):
        ans +=1
    # 아니면 pass 한다.
    else:
        pass
        
print(ans)