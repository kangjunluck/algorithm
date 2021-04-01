import sys

input = sys.stdin.readline

n, m = map(int, input().split())

data = [0 for _ in range(n)]
for i in range(n):
    data[i] = input()
ans =0
for j in range(m):
    check = input()
    if check in data:
        ans+=1
print(ans)
# def find(start, check_dot ,alpha, x, y):
#     cnt = 1
#     for k in range(start+1, x-(y-1-check_dot)):
#         if ele[k] == alpha:
#             return cnt
#         cnt += 1
#     return cnt

# def bm(ele, check):
#     x = len(ele)
#     y = len(check)

#     # ele에서 시작점 : 변경될것이다.
#     a = 0
#     while a <= x-y:
#         # check할 단어의 시작점(맨 뒤부터)-
#         b = y-1

#         while b>=0:
#             if check[b] != ele[a+b]:
#                 change = find(a+b, b, check[b], x, y)
#                 break
#             b -= 1
#         if b == -1:
#             return True
#         else:
#             a += change
#     return False

# ans = 0
# for j in range(m):
#     check = input()
#     for ele in data:
#         if bm(ele, check):
#             ans += 1
#             print(ele, '이게 ele')
#             print(check, '이게 check')
# print(ans)