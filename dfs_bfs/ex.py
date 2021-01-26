from itertools import combinations

for i in combinations([(1,2),(3,4),(5,6)], 2):
    for a,b in i:
        print(a,b)