from itertools import permutations
from itertools import combinations

data = 'abcded'
cnt = 0
for perm in permutations(data, 3):
    cnt += 1
    print(perm)
print(cnt)