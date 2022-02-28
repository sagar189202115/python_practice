a=[4,2,7,1,3]
k=10
dp=[[0 for i in range(k+1)] for j in range(len(a)+1)]
for i in range(len(a)):
    for j in range(k+1):
        if i==0 and j==0:
            dp[i][j]=1
        elif a[i-1]>j:
            dp[i][j]=dp[i-1][j]
        else:
            val=a[i-1]
            if dp[i-1][j]==1 or dp[i-1][j-val]==1:
                dp[i][j]=1
print(dp[-1][-1])