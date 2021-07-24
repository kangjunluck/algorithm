n = int(input())
data = list(map(str,input().split()))

numa = [i for i in range(10)]
numb = [j for j in range(9, -1, -1)]
# 오름차순 먼저  조합으로 하면, 다 돌게 된다. 처음 나온 값으로 끊을 수가 없어

def combi(idx, before, nums):
    global isAnswer
    if isAnswer:
        return
    if idx == n+1:
        print(''.join(sel))
        isAnswer = True
        return
    for i in range(10):
        if check[i]: continue
        check[i] = 1
        if idx == 0:
            sel[idx] = str(nums[i])
            combi(idx+1, nums[i], nums)
        else:
            if data[idx-1] == '<':
                if before < nums[i]:
                    sel[idx] = str(nums[i])
                    combi(idx+1, nums[i], nums)
            else:
                if before > nums[i]:
                    sel[idx] = str(nums[i])
                    combi(idx+1, nums[i], nums)
        check[i] = 0


check = [0]*(10)
sel = [-1]*(n+1)
isAnswer = False
combi(0, 0, numb)
    
sel = [-1]*(n+1)
check = [0]*(10)
isAnswer = False
combi(0, 0, numa)