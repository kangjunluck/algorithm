n = int(input())
nums = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
i = 1
while i < n:
    newnums = [0 for _ in range(10)]
    for j in range(10):
        if j == 0:
            newnums[j] = nums[j+1]
        elif j == 9:
            newnums[j] = nums[j-1]
        else:
            newnums[j] = nums[j-1] + nums[j+1]
    nums = newnums
    i += 1
    
print(sum(nums)%1000000000)