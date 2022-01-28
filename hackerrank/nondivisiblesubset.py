s=list(map(int,input().split()))
k=4
r=[0]*k
maxx=0
for i in s:
    r[i%k]+=1
maxx+=min(r[0],1)
if(k)%2==0:
    maxx+=min(r[k//2],1)
    for i in range(1,(k//2)):
        if i!=k-i:
            maxx+=max(r[i],r[k-i])
print(maxx)
