a=-1
b=1
n=7
for x in range(0,n+1):
    temp=a+b
    if(x==n):
        print(a+b)
    a=b
    b=temp
    
