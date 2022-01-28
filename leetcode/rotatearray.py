nums=[1,2,3,4,5,6,7]
k=3
for x in range(0,k+1):
    temp=arr[x+k+1]
    arr[x+k+1]=arr[x]
