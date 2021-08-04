n = int(input())
sequence = list(map(int,input().split()))

# 조합/백트래킹을 이용하여 구하는 방법이 잇을 거다
# 하지만 이건 이분 탐색이다. 다르게 접근한다
# 하나씩 탐색하는데 크면 그냥 넣고 작으면 어디 위치와 교환시킬지 고른다.
# 실제 수열과 LIS(Longest Increasing Sequence) 결과랑 값은 다르다 왜? 감소하더라도 교환해주기 때문!

seq = [0] # 나중에 빼주면 된다. 넣고 시작하자 

for case in sequence:
    if seq[-1] < case:
        seq.append(case)

    else:
        # 어디 위치랑 바꿀 건지 이진탐색
        l = 0
        r = len(seq)
        while l < r:
            mid = (l+r)//2
            if seq[mid]<case:
                l = mid + 1
            else:
                r = mid
        seq[r] = case

print(len(seq)-1)