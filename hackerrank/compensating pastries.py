n=int(input())
arr=list(map(int,input().split()))
c=[1 for i in range(len(arr))]
for i in range(len(arr)-1):
    if arr[i+1]<arr[i]:
        c[i+1]=c[i]+1
for i in range(len(arr)-1,0,-1):
    if arr[i-1]<arr[i] and c[i-1]<=c[i]:
        c[i-1]=c[i]+1
print(sum(c))