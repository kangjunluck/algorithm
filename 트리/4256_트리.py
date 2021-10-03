T = int(input())
i = 0
for tc in range(1,T+1):
    n = int(input())
    preorder = list(map(int,input().split()))
    inorder = list(map(int,input().split()))

    
    answer = []
    def makeAns(part):
        global i
        now = preorder[i]
        i += 1
        idx = part.index(now)
        if part[:idx] != []:
            makeAns(part[:idx])
        if part[idx+1:] != []:
            makeAns(part[idx+1:])
        answer.append(now)
    
    makeAns(inorder)
    print(*answer)
    i = 0