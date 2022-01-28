n,m=map(int,input().split())
arr=["" for i in range(n)]
for i in range(n):
    arr[i]=input()
c=0
for i in range(n):
    for j in range(m):
        if(arr[i][j]=='a'):
            if(j<=m-3 and arr[i][j+1]=="b" and arr[i][j+2]=="c"):
                c+=1
            if(i<=n-3 and arr[i+1][j]=='b' and arr[i+2][j]=='c'):
                c+=1
            if(j>=2 and i<=n-3 and arr[i+1][j-1]=='b' and arr[i+2][j-2]=='c'):
                c+=1
            if(j<=m-3 and i<=n-3 and arr[i+1][j+1]=='b' and arr[i+2][j+2]=='c'):
                c+=1
print(c)
