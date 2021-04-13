# import sys

# input = sys.stdin.readline

# info = {
#     'I' : 1,
#     'V' : 5,
#     'X' : 10,
#     'L' : 50,
#     'C' : 100,
#     'D' : 500,
#     'M' : 1000,
# }
# ecp = {
#     'IV' : 4,
#     'IX' : 9,
#     'XL' : 40,
#     'XC' : 90,
#     'CD' : 400,
#     'CM' : 900,
# }
# # total = {
# #     'M' : 1000,
# #     'CM' : 900,
# #     'CD' : 400,
# #     'D' : 500,
# #     'C' : 100,
# #     'XC' : 90,
# #     'L' : 50,
# #     'XL' : 40,
# #     'X' : 10,
# #     'IX' : 9,
# #     'V' : 5,
# #     'IV' : 4,
# #     'I' : 1,
# # }
# check = list(ecp.keys())

# A = input().strip()
# B = input().strip()
# a = list(A)
# b = list(B)
# numa = 0
# na = len(A)
# nb = len(B)

# i = 0
# while i < na:
#     if (A[i] == 'I' or A[i] == 'X' or A[i] == 'C') and i != na-1:
#         duo = ''
#         duo += a[i]
#         duo += a[i+1]
#         if duo in check:
#             numa += ecp[duo]
#             i += 2
#         else:
#             numa += info[a[i]]
#             i += 1
#     else:
#         numa += info[a[i]]
#         i += 1
# j = 0
# while j < nb:
#     if (B[j] == 'I' or B[j] == 'X' or B[j] == 'C') and j != nb-1:
#         duo = ''
#         duo += b[j]
#         duo += b[j+1]
#         if duo in check:
#             numa += ecp[duo]
#             j += 2
#         else:
#             numa += info[b[j]]
#             j += 1
#     else:
#         numa += info[b[j]]
#         j += 1
# print(numa)


def make_num(word):
    result = 0
    for c in to_num.keys():
        while word.startswith(c):
            result += to_num[c]
            word = word[len(c):]
    return result

def make_word(num):
    result = ""
    for n in to_st.keys():
        while num >= n:
            result += to_st[n]
            num -= n
    return result

to_num = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1}
to_st = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}

a = input().strip()
b = input().strip()

sum = make_num(a) + make_num(b)
print(sum)
print(make_word(sum))