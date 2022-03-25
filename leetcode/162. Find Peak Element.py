import math


def peakelement(nums):
    maxx=0
    nums.append(-math.inf)
    i=0
    while i<len(nums):
        if nums[i]>nums[maxx]:
            if nums[i]>nums[i+1]:
                maxx=i

            if nums[i+1]>nums[i]:
                i+=1
            else:i+=2
        else:i+=1
    return maxx
print(peakelement([1,2,4,3,5,6,8,0,7]))
