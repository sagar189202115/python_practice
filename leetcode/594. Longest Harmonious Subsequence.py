def findLHS(nums):
    d={}
    res=0
    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]]=1
        else:
            d[nums[i]]+=1
    for i in d:
        if i+1 in d:
            res=max(res,d[i]+d[i+1])
    return res
print(findLHS([1,3,2,2,5,2,3,7]))
