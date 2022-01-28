def isBadVersion(n):
    if(n>=1):
        return True
    return False
i=5

h=i
l=1
m=(l+h)//2

while(h>=l):
    if(isBadVersion(m)):
        h=m-1
        
    else:
        l=m+1
        
    
    m=((l+h)//2)
print(m+1)

