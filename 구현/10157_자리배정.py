#이거 달팽이랑 비슷하다. 냄새가 난다.
import sys

input = sys.stdin.readline

n, m = map(int,input().split())
want = int(input())
num = 1
i, j = 0, 0
dr = [1, 0, -1, 0] # 위 오른쪽 아래 왼쪽
dc = [0, 1, 0, -1]
height = m-1
weight = n-1
end = n * m
ans = []
roof = 1
while roof > 0:
    for way in range(4):
        if way%2 == 0:
            for a in range(height):
                if num == want:
                    ans.append((j+1, i+1))
                    roof = 0
                    break
                if num == end:
                    roof = 0
                    break
                i = i + dr[way]
                j = j + dc[way]
                num += 1           
                
        else:
            for b in range(weight):
                if num == want:
                    ans.append((j+1, i+1))
                    roof = 0
                    break
                if num == end:
                    roof = 0
                    break
                i = i + dr[way]
                j = j + dc[way]
                num += 1
                
    i += 1
    j += 1
    height -= 2
    weight -= 2
if ans:
    print(ans[0][0], ans[0][1])
else:
    print(0)