import math
def oddsum(a,b):
    if a%2==0:
        a+=1
    if b%2==0:
        b-=1
    return (math.ceil(b/2)**2)-(a//2)**2
def evensum(a,b):
    if a%2==1:
        a+=1
    if b%2==1:
        b-=1
    a=(a-2)//2
    b=b//2
    return ((b**2)+b)-((a**2)+a)
(a,b)=map(int,input().split())
print(evensum(a,b),oddsum(a,b))
print(abs(oddsum(a,b)-evensum(a,b)))