m=3
arr=[3,1,4,2]

n=len(arr)

print(a)
lis=[1]*n*m
for i in range(m):
    maxx=0
    for j in range(n):
        print(j+(n*i))
        if arr[i-n]>=arr[j-n] and lis[j+(n*i)]>maxx:

            maxx=lis[i]
        lis[i]=maxx+1
print(lis)