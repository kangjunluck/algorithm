def solution(orders, course):
    answer = []
    n = len(orders)                
    def alphaCnt(word1, word2):
        cnt = 0
        part = ''
        n1 = len(word1)
        n2 = len(word2)
        for i in range(n1):
            for j in range(n2):
                if word1[i] == word2[j]:
                    cnt += 1
                    part += word1[i]
        return cnt, part           
                
    for i in range(n-1):
        for j in range(i+1, n):
            cnt, part = alphaCnt(orders[i], orders[j])
            if cnt in course:
                answer.append(part)
    answer = sorted(answer)
    return answer