import sys

input = sys.stdin.readline
T = int(input())
for case in range(1,T+1):
    n =int(input())
    board = list(map(int, input().split()))

    for i in range(len(board)-1, 0, -1):
        for j in range(0, i):
            if board[j] > board[j+1]:
                board[j], board[j+1] = board[j+1], board[j]
    new_list = []
    if n%2:
        for k in range(n//2):
            if len(new_list) == 10:
                break               
            if n-1-k != k:    
                new_list.append(str(board[n-1-k]))
                new_list.append(str(board[k]))
            else:
                new_list.append(str(board[k]))
    else:
        for k in range(n//2):
            if len(new_list) == 10:
                break 
            new_list.append(str(board[n-1-k]))
            new_list.append(str(board[k]))
    change = ' '.join(new_list)
    print('#{} {}'.format(case,change))