import sys

input = sys.stdin.readline

total = 0
trees = dict()
while True:
    tree = input().rstrip()
    if not tree:
        break
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1
    total += 1
treesort = sorted(list(trees.keys()), key = lambda x:x)

for i in treesort:
    print("{} {:.4f}".format(i, trees[i]/total*100))