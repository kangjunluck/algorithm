n, h = map(int,input().split())

up = [0 for _ in range(h + 1)]
down = [0 for _ in range(h + 1)]
for i in range(n):
    num = int(input())
    if i%2:
        up[num] += 1
    else:
        down[h - num + 1] += 1
print(up)
print(down)
# for j in range(h)
