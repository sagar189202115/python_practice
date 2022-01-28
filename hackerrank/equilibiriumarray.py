arr = [int(input()) for i in range(0, 5)]
su=sum(arr)
s=0
flag=0
ans=0
for i in range(5):
    su -= arr[i]
    if su == s:
        flag= 1
        ans=i+1
    s+=arr[i]
if flag:
    print(ans)
else:
    print(-1)


