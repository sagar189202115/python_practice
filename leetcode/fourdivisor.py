nums=[x for x in range(1,10000000)]
t=5000
for x in nums:
    n=s=0
    n1=0
    n2=0
    for y in range(2,(x//2)+1):
        if(x%y==0):
            n+=1
            s+=y
            if(n==1):n1=y
            if(n==2):n2=y
        if(n>2):
            break
    if(n==2 and n2%2==0):
        t=t+s+1+x
        print(x,n1,n2)
#if(t!=0):
#    print(t)
#else:print(0)
