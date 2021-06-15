def solution(p):
    answer = ''
           
    
    def makeAns(word):
        print(word)
        n = len(word)
        v = ''
        u = ''
        t = 0
        for i in range(n):
            # ( 일때
            if word[i] == '(':
                u += '('
                t += 1    
            # ) 일때
            else:
                u += ')'
                t -= 1
            if t == 0:
                if i != n-1:
                    v = word[i+1:]
                break
                
        if v != '':
            v = makeAns(v)
            
        if u[0] == ')':
            u = u[1:-1]
            re_u = ''
            for i in range(len(u)):
                if u[i] == '(':
                    re_u += ')'
                else:
                    re_u += '('
            
            return '(' + v + ')' + re_u
        
        return u + v

    answer = makeAns(p)     
        

    
    return answer