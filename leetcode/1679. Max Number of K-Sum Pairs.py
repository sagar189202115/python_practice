def operations(nums,k):
    nums.sort()
    c = 0
    i = 0
    j = len(nums) - 1
    while i < j:
        if (nums[i] + nums[j]) == k:
            c += 1
            i += 1
            j -= 1
        elif (nums[i] + nums[j]) > k:
            j -= 1
        else:
            i += 1
    return c
print(operations([1,3,3,3,4],6))