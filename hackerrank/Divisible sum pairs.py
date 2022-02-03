l=[1,2,3,4,5,6]
k=5
ans=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if (l[i]+l[j])%k==0:
            ans.append([l[i],l[j]])

print(ans)
