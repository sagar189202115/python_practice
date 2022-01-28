nums=[-4,-1,0,3,10]
newarr=[]
maxx=nums[0]*nums[0]
for x in nums:
    newarr.append(x*x)
print(sorted(newarr))
