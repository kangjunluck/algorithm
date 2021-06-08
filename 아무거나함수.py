enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

def solution(enroll, referral, seller, amount):
    answer = []
    # 후위 순회, 부모를 가장 나중에, 그래야 자식들의 이익을 다 담는다.
    # enroll 참여자, referral 부모
    # seller 판매자, amount 판매자가 판 양
    n = len(enroll)
    m = len(seller)
    
    sub = [[] for _ in range(n)]
    income = dict()
    idx = dict()
    start = []
    for i in range(n):
        if referral[i] == '-':
            start.append(i)
        income[enroll[i]] = 0
        idx[enroll[i]] = i
        for j in range(n):
            if referral[j] == enroll[i]:
                sub[i].append(j)
                
    for i in range(m):
        income[seller[i]] += amount[i] * 100 
    
    def findans(k):
        # 후위 순회
        for son in sub[k]:
            findans(son)
            
        if referral[k] == '-':
            income[enroll[k]]  -= (income[enroll[k]])//10
        else:
            income[referral[k]] += (income[enroll[k]])//10
            income[enroll[k]]  -= (income[enroll[k]])//10
        return
                    
    for k in start:
        findans(k)

    for a in income.values():
        answer.append(a)
    return answer


solution(enroll, referral, seller, amount)