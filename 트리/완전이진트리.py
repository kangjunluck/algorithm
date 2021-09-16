k = int(input())
datas = list(map(int, input().split()))

answer = [[] for _ in range(k)]

# 탐색하는게 아니라 data를 보고 구조를 확인하는 것

# 중앙값이 그 단계의 노드 값이다

def makeAns(step, s, e):
    print(step, s, e)
    mid = (s+e)//2
    answer[step].append(str(datas[mid]))
    if s == e:
        return
    makeAns(step+1, s, mid-1)
    makeAns(step+1, mid+1, e)

makeAns(0, 0, len(datas)-1)
for i in answer:
    print(' '.join(i))