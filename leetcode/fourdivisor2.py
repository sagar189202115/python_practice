#nums=[x for x in range(1,10000000)]
nums=[86]
t=0
for x in nums:
    n=s=0
    for y in range(2,(x//2)+1):
        if(x%y==0):
            flag=1
            for z in range(2,((x//y)//2)+1):
                if((x//y)%z==0):
                    flag=0
                    break
            if(flag):
                s=s+y+(x//y)
                break
    t=t+s+1+x 
        
        
if(t!=0):
    print(t)
else:print(0)
