def pima(nums):
    nums.append(0)
    h=len(nums)-1
    l=0
    m=(l+h)//2
    while not(nums[m+1]<nums[m]>nums[m-1]):
        if nums[m]<nums[m-1]:
            h=m-1
            m=(l+h)//2
        else:
            l=m+1
            m=(l+h)//2

    return m
print(pima([0,2,1,0]))
