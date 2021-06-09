T = int(input())

for tc in range(1,T+1):
    n = int(input())
    data = [list(map(int,input().split())) for _ in range(n)]
    check = [0 for _ in range(n)]

    maxi = 0
    def perm(idx, totalH=0, x1=10000, y1=10000):
        global maxi
        if maxi < totalH:
            maxi = totalH
        if idx == n:
            return

        for i in range(n):
            if check[i]: continue
            check[i] = 1
            # 3가지 경우를 나누어서. 각 변이 높이가 되는 경우
            for j in range(3):
                if j == 0:
                    a = data[i][1]
                    b = data[i][2]
                    h = data[i][j]
                elif j == 1:
                    a = data[i][0]
                    b = data[i][2]
                    h = data[i][j]
                else:
                    a = data[i][0]
                    b = data[i][1]
                    h = data[i][j]
                if (x1>= a and y1 >= b) or (y1 >= a and x1 >= b):
                    perm(idx+1, totalH+h, a, b)    
            check[i] = 0
            
    perm(0)
    print('#%d %d' %(tc, maxi))