import sys
sys.setrecursionlimit(10**6)

n = int(input())

inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

inorderidx = [0 for _ in range(n+1)]
for i in range(n):
    inorderidx[inorder[i]] = i

# 와 어렵다 이거
def findans(l_in, r_in, l_post, r_post):
    if l_in > r_in or l_post > r_post:
        return
    
    parent = postorder[r_post]
    print(parent, end=" ")

    thick = inorderidx[parent] - l_in

    findans(l_in, inorderidx[parent]-1, l_post, l_post + thick-1)
    findans(inorderidx[parent]+1, r_in, l_post+thick, r_post-1)

findans(0, n-1, 0, n-1)