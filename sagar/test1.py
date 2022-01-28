import math

s="feedthedog"
c=0
i=math.floor(math.sqrt(len(s)))
j=math.ceil(math.sqrt(len(s)))
l=""
if i*j<len(s):
    i+=1
n=[["" for x in range(0,i)] for y in range(0,j)]

x=0
z=0
while True:
    if(z>=len(s)):
        break
    elif(x==j):
        x=0
        c+=1
    n[x][c]=s[z]
    
    x+=1
    z+=1
for x in n:
    for y in x:
        l+=y
    l+=" "
    
    

print(l)


