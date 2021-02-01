import sys

sys.stdin = open('1996.txt', 'r')
input = sys.stdin.readline

cases = int(input())


for case in range(cases):
    cnt = 0
    n, i = map(int, input().split())
    
    board = list(map(int, input().split()))
    visited = [0 for _ in range(n)]
    visited[i] = 1
    while True:
        out = board.pop()
        out_visit = visited.pop()
        
        if out_visit == 1:
            cnt += 1
            break
        else:
            check_list = [ nu for nu in range(out+1, 10) if nu in board ]
            if check_list:
                if board.index(check_list[-1]) > i:
                    trash = visited.pop()
                    board.remove(check_list[-1])
                    cnt += 1
                elif board.index(check_list[-1]) == i:
                    cnt += 1
                    break
                else:
                    board.remove(check_list[-1])
                    cnt += 1
            else:
                cnt +=1
                                        
    print(cnt)