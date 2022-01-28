def isBadVersion(n):
    if(n>=1):
        return True
    return False
i=[1,3,5,6]

h=len(i)-1
l=0
m=(l+h)//2
t=2
while(h>=l):
    if(i[m]>t):
        h=m-1
        
    else:
        l=m+1
        
    
    m=((l+h)//2)
if(i[m]==t):
    print(m)
else:
    print (m+1)

