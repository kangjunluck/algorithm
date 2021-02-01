import sys

input = sys.stdin.readline

n = list(map(int,input().strip()))

# 반복하니까 재귀? 그냥 했더니 됐다.
# 옆집에서 숫자 사다가 보관하는 박스를 만들었다.
box = []
cnt = 0
# 천천히 한단계씩 생각해보자.
for num in n:
    # 6, 9인지 아닌지가 중요해서 나누었다.
    # 이후 그 숫자가 있는지, 그리고 뒤집혀 진게 있는지로 나누어야 한다.
    if num == 6 or num == 9:
        if 6 in box or 9 in box:
            if num in box:
                box.remove(num)
            else: # 리스트 빼기 부분인데.. 도저히 방법이 없어서 원소를 뺏다.
                change = [6, 9]
                change.remove(num)
                box.remove(change[0])
        # 박스에 6, 9가 없으면 세트 하나 넣어주고 하나 사용하자.
        else:
            box += [1,2,3,4,5,6,7,8,9,0]
            cnt += 1
            box.remove(num)
    # 6,9가 아니면 쉽다 넣어주고 cnt 해주고
    else:
        if num in box:
            box.remove(num)
        else:
            box += [1,2,3,4,5,6,7,8,9,0]
            cnt += 1
            box.remove(num)

print(cnt)



import sys

input = sys.stdin.readline

# 방번호
room = int(input())
# 빙반호 복사
clone = room
# 몇 세트가 쓰였는지 확인용도
set_number = [0 for _ in range(10)]
# 6과 9 체크
check = 0
# 답
answer = 0


######### 다른 풀이 이해해 보기

# while room > 0:
#     # 방번호중 끝번호를 인덱스로 사용 EX) 9999 -> 9
#     idx = room % 10
#     # 방번호는 한자리 줄여준다
#     room //= 10
#     # 인덱스에 하나 추가
#     set_number[idx] += 1

#     # 만약 인덱스가 6이나 9인데 체크하는게 1이면(6또는 9가 2번나왔으면)
#     if (idx == 6 or idx == 9) and check == 1:
#         # 그 인덱스 번호 하나 줄여주고 체크는 다시 0으로
#         set_number[idx] -= 1
#         check = 0
#     # 만약 인덱스가 6이나 9인데 체크가 안되있으면
#     elif (idx == 6 or idx == 9) and check == 0:
#         # 체크를 1로 바꿔줌
#         check = 1

# # 만약 원래 숫자가 10이라면  while문을 수행안하니깐 그냥 1세트썻다고 적어줌 
# if clone < 10:
#     answer = 1
# else:
#     # 6과 9를 더해주고 하나는 초기화
#     set_number[6] += set_number[9]
#     set_number[9] = 0
#     # 최대값이 총 사용한 세트개수
#     answer = max(set_number)

# print(answer)