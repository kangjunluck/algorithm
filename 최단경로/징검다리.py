rocks = [2, 14, 11, 21, 17]

answer = 0
# m = len(rocks)
rocks.sort()
print(rocks)

# def check(mid):
#     i = cnt = 0
#     before = 0
#     while i < m:
#         if rocks[i] - before >= mid:
#             before = rocks[i]
#         else:
#             if cnt == 2:
#                 return False
#             else:
#                 cnt += 1
#         i += 1
#     return True
# l = 0
# r = distance
# while l < r:
#     mid = (l + r)//2
#     if check(mid): l = mid
#     else: r = mid - 1