#수학문제
# 잘린 사각형의 갯수가 w+h-최대공약수란다


def solution(w,h):
    #4개의 꼭지점이 한쪽에 있어야 한다.
    #함수는 구해야 한다
    # h/w *x = y
    total = h * w
    for j in range(h):
        for i in range(j*w//h, w):
            #나머지를 가지치기 i,j랑 i, j+1이 우 상단이면 pass
            if j+1 <= h/w*i:
                continue
            # (i+1,j), (i, j+1) 두 좌표가 그래프의 양 쪽에 있어야 한다.
            if ((h/w * (i+1)) - j) *((h/w * i) - (j+1)) < 0:
                total -= 1
            
            w*h - (w+h-최대공약수)
    answer = total
    return answer