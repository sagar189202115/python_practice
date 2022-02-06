d={}
nums=[0,0,1,1,1,2,2,3,3,4]
c=0
i=0
while i <len(nums):
    if nums[i] not in d:
        d[nums[i]]=1
        i+=1
    elif nums[i] in d:
        nums.remove(nums[i])
        c+=1
print(nums)