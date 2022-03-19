nums = [2,2,2,2,2]
key = 2
k = 2
res=[]
dic={}
d=[]
for i in range(len(nums)):
    if nums[i]==key:
        d.append(i)
i=0
j=0
for i in range(len(d)):
    for j in range(max(0,d[i]-k),d[i]+k+1):

        if j<len(nums) and j not in dic:
            dic[j]=1
            res.append(j)


print(res)